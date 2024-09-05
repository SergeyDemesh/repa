import datetime

from django.db import models
from django.contrib import admin


class Student(models.Model):
    first_name = models.CharField(max_length=30, default='', verbose_name='First name')
    last_name = models.CharField(max_length=30, default='', verbose_name='Last name')
    balance = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Balance')
    class_cost = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Class cost')
    phone = models.CharField(max_length=13)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Payment(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(default=datetime.date.today())
    customer = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} {self.amount}"


class Lesson(models.Model):
    date = models.DateField(default=datetime.date.today())
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_time = models.TimeField(verbose_name="Start time")
    end_time = models.TimeField(verbose_name="End time")
    state = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.student} {self.date}"
