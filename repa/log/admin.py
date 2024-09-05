from django.contrib import admin

from .models import Student, Payment, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 3


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal', {'fields': ['first_name', 'last_name', 'balance', 'class_cost', 'active']})
    ]
    list_display = ['first_name', 'last_name', 'balance', 'class_cost']
    inlines = [LessonInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'state', 'amount']


admin.site.register(Student, StudentAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Payment)
