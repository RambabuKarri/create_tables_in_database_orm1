from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.dept_name

    

class Emp(models.Model):
    emp_no=models.IntegerField()
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    doj=models.DateField()
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ename

