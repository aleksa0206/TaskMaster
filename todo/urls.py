from django.contrib import admin
from django.urls import path
from . import views
from .views import TaskCreate,TaskUpdate,TaskDelete

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('login/',views.loginPage,name='login'),
    path('moderator-dashboard/', views.moderatorPage, name='moderator-dashboard'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('logout/',views.logout,name='logout'),
    path('',views.homePage, name='home'),
    path('contact/',views.contactPage,name='contact'),
    path('about/',views.aboutPage,name='about'),
    path('smart/',views.smartPage,name='smart'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),

    # path('admin/', admin.site.urls, name='admin'),


]