from django.db import models

# Create your models here.

class Degree(models.Model):
    title = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)
    
    def __str__(self):
        template = '{0.title} {0.branch}'
        return template.format(self)

class Student(models.Model):
    roll_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    dob = models.DateField('date of birth')
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    
    def __str__(self):
        template = '{0.roll_number} {0.name} {0.degree} {0.year} {0.dob} '
        return template.format(self)
        #return (self.roll_number, self.name, self.degree)