from django.db import models
from django.core.validators import RegexValidator


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Purpose(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


GEN_CHOICES = [('M', 'Male'), ('F', 'Female'), ]


class Person(models.Model):
    name = models.CharField(max_length=124)
    date_field = models.DateField(auto_now=False,null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=40, choices=GEN_CHOICES)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=200)
    address = models.TextField(max_length=300)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    Purpose = models.ForeignKey(Purpose, on_delete=models.SET_NULL, blank=True, null=True)
    pen = models.BooleanField(default=False)
    note_book = models.BooleanField(default=False)
    exam_paper = models.BooleanField(default=False)

    def __str__(self):
        return self.name
