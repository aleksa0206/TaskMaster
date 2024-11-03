from django.db import models

# Create your models here.




class Task(models.Model):
    CATEGORY = [
        ('Not Started','Not Started'),
        ('In progress','In progress'),
        ('Completed','Completed')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=200,choices=CATEGORY,default='Not Started')

    def __str__(self):
        return self.title