from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length =400)
    address = models.CharField(max_length = 300)
    zip_code = models.IntegerField()


    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField()
    date_of_resumption = models.DateField(default =datetime.today)

    def __str__(self):
        return self.first_name