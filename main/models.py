from django.db import models
from django.utils import timezone
    
class Supervisor(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=7, unique=True)
    def __str__(self):
        return self.name
    
class Notes(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    def __str__(self):
        return self.note
    
class User(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    project_name = models.CharField(max_length=20)  
    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateField()
    task_heading = models.CharField(max_length=20, unique=True)
    task_details = models.CharField(max_length=250)
    progress = models.DecimalField(max_digits=4, decimal_places=1, default = 0.0)
    timestamp = models.DateTimeField()
    def __str__(self):
        return self.task_heading
