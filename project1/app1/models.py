from django.db import models

# Create your models here.

class Employees(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField(unique=True)

    def __str__(self):
        return "Firstname:{} , Lastname:{}".format(self.firstname,self.lastname)