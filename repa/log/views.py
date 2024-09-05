import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .scripts import views_helper

from .models import *


class StudentsListView(generic.ListView):
    model = Student
    template_name = 'log/students_list.html'
    ordering = 'last_name'
    context_object_name = 'students_list'

    def get_context_data(self, **kwargs):
        context = super(StudentsListView, self).get_context_data(**kwargs)
        context['sum'] = sum( [student.balance for student in Student.objects.filter(balance__lte=0)])
        context['students_list'] = Student.objects.filter(active=True)
        return context


class StudentView(generic.DetailView):
    model = Student
    template_name = 'log/student.html'


def change_lesson_state(request, student_id):
    student = Student.objects.get(pk=student_id)
    lesson_list = student.lesson_set.all()
    data = json.loads(request.body)
    data_str = data['data'].replace('\\"', '')
    data_list = data_str.split(',')
    data_dict = {}
    for i in range(len(data_list)):
        data_list[i] = data_list[i].split(':')
        data_list[i][0] = int(data_list[i][0].replace('"{', ''))
        data_list[i][1] = False if data_list[i][1].replace('}"', '') == "false" else True
    for data in data_list:
        data_dict.update({data[0]: data[1]})
    for lesson in lesson_list:
        if lesson.state != data_dict[lesson.id]:
            lesson.state = data_dict[lesson.id]
            student.balance = student.balance - lesson.amount if lesson.state else student.balance + lesson.amount
    Lesson.objects.bulk_update(lesson_list, ['state'])
    student.save()
    return HttpResponseRedirect(reverse("log:student", args=(student.id,)))


def show_add_payment_form(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {'student': student}
    return render(request, 'log/add_payment.html', context)


def add_payment(request, student_id):
    student = Student.objects.get(pk=student_id)
    amount = int(request.POST['amount'])
    date_str_list = request.POST['date'].split('-')
    date_payment = datetime.date(int(date_str_list[0]), int(date_str_list[1]), int(date_str_list[2]))
    new_payment = Payment(amount=amount, date=date_payment, customer=student)
    new_payment.save()
    student.balance = sum([payment.amount for payment in student.payment_set.all()]) - [lesson.state for lesson in student.lesson_set.all()].count(True) * student.class_cost
    student.save()
    return HttpResponseRedirect(reverse("log:student", args=(student.id,)))


def show_add_lesson_form(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {'student': student}
    return render(request, 'log/add_lesson.html', context)


def add_lesson(request, student_id):
    student = Student.objects.get(pk=student_id)
    date_str_list = request.POST['date'].split('-')
    start_time_str_list = request.POST['start_time'].split(':')
    end_time_str_list = request.POST['end_time'].split(':')
    date_lesson = datetime.date(int(date_str_list[0]), int(date_str_list[1]), int(date_str_list[2]))
    start_time = datetime.time(int(start_time_str_list[0]), int(start_time_str_list[1]))
    end_time = datetime.time(int(end_time_str_list[0]), int(end_time_str_list[1]))
    lesson = Lesson(date=date_lesson, start_time=start_time, end_time=end_time, student=student, state=False, amount=student.class_cost)
    lesson.save()
    return HttpResponseRedirect(reverse("log:student", args=(student.id,)))
