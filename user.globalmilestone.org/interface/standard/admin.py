from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Student, Tutor, Session, Course, CourseInstance, PackageCourse, PackageInstance


class CourseInstanceItem(admin.ModelAdmin):
    search_fields = ['parent_course__full_name', 'parent_course__abbrev_name']
    filter_horizontal = ['tutors']

class TutorItem(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']

class SessionItem(admin.ModelAdmin):
    autocomplete_fields = ['parent_course_instance']
    filter_horizontal = ['students_attending','students_attended','tutors','monitors']
    search_fields = ['start_time','parent_course_instance__parent_course__abbrev_name']

admin.site.register(Student)
admin.site.register(Tutor, TutorItem)
admin.site.register(Session, SessionItem)
admin.site.register(Course)
admin.site.register(CourseInstance, CourseInstanceItem)
admin.site.register(PackageCourse)
admin.site.register(PackageInstance)
