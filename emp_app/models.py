from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=255)
    salary=models.IntegerField(default=0)
    location=models.CharField(max_length=255)

    def __str__(self) :
        return self.dept_name 

class Role(models.Model):
    role_name=models.CharField(max_length=255)
    def __str__(self) :
        return self.role_name 

class Employee(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dept=models.ForeignKey(Department, on_delete=models.CASCADE)
    bonous=models.IntegerField(default=0)
    role=models.ForeignKey(Role, on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hire_date=models.DateField()

    def __str__(self) :
        return self.first_name 

