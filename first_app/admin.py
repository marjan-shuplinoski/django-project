from django.contrib import admin
from .models import Course, Instructor, Enrollment, Participant


# Register your models here.

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_of_participants', 'start_date', 'number_of_classes', 'description']
    list_filter = ['name','category','instructorID', 'number_of_participants','price']

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'city']


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['courseID', 'participantID']


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'city']


admin.site.register(Course, CoursesAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Participant,ParticipantAdmin)
