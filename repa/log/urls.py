from django.urls import path

from . import views

app_name = 'log'
urlpatterns = [
    path('', views.StudentsListView.as_view(), name='students_list'),
    path('<int:pk>/', views.StudentView.as_view(), name='student'),
    path('<int:student_id>/add_payment', views.add_payment, name='add_payment'),
    path('<int:student_id>/add_lesson', views.add_lesson, name='add_lesson'),
    path('<int:student_id>/save', views.change_lesson_state, name='student_save'),
    path('<int:student_id>/payment_form', views.show_add_payment_form, name='student_payment_form'),
    path('<int:student_id>/lesson_form', views.show_add_lesson_form, name='student_lesson_form'),
]
