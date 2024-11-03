from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import *
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from .decorators import group_based_redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_dashboard(request):
    completed_tasks = Task.objects.filter(status='completed')
    in_progress_tasks = Task.objects.filter(status='in progress')
    not_started_tasks = Task.objects.filter(status='not started')

    context = {
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
        'not_started_tasks': not_started_tasks,
    }


    return render(request,'accounts/user_dashboards.html',context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.groups.filter(name='user').exists():
                return redirect('user-dashboard')
            elif user.groups.filter(name='moderator').exists():
                return redirect('moderator-dashboard')
            elif user.groups.filter(name='admin').exists():
                return redirect('admin:index')  # Preusmeri na Django admin stranicu
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'accounts/login.html')


def contactPage(request):
    return render(request,'accounts/contact.html')

def moderatorPage(request):
    completed_tasks = Task.objects.filter(status='Completed')
    in_progress_tasks = Task.objects.filter(status='In progress')
    not_started_tasks = Task.objects.filter(status='Not Started')
    total_users = User.objects.count()  # Prebrojava sve korisnike
    total_tasks = Task.objects.count()  # Prebrojava sve taskove


    
    
    context = {
        'completed_tasks': completed_tasks,
        'in_progress_tasks': in_progress_tasks,
        'not_started_tasks': not_started_tasks,    
        'total_users': total_users,
        'total_tasks': total_tasks,
    }

    return render(request, 'accounts/moderator_dashboard.html',context)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('moderator-dashboard')
    template_name = 'accounts/task_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('moderator-dashboard')
    template_name = 'accounts/task_form.html'  # Ispravna putanja do šablona

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('moderator-dashboard')

def logout(request):
    auth_logout(request)  # Ovo odjavljuje korisnika
    return redirect('login')  # Preusmerava na stranicu za prijavu

def homePage(request):
    return render(request,'accounts/home.html')


def aboutPage(request):
    return render(request,'accounts/about.html')

def smartPage(request):
    return render(request,'accounts/smart.html')