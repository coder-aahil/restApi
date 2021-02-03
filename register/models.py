from django.db import models

# Create your models here.

class Client(models.Model):
    client_name=models.CharField(max_length=250)
    created_at=models.DateTimeField()
    created_by=models.CharField(max_length=100)

    def __str__(self):
        return self.client_name
class Project(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    project_name=models.CharField(max_length=250)
    

    def __str__(self):
        return self.project_name
