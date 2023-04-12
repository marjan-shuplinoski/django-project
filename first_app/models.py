from django.db import models


# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    linkedin_link = models.URLField()
    github_link = models.URLField()


class Course(models.Model):
    name = models.CharField(max_length=100)
    number_of_participants = models.IntegerField()
    start_date = models.DateTimeField()
    number_of_classes = models.IntegerField()
    description = models.CharField(max_length=150)
    price = models.IntegerField()
    programming = 'Prog'
    marketing = 'Mark'
    soft_skills = 'Soft'
    category_choices = [
        (programming, 'Programming'),
        (marketing, 'Marketing'),
        (soft_skills, 'Soft Skills'),
    ]
    category = models.CharField(
        max_length=4,
        choices=category_choices,
        default=programming,
    )
    instructorID = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)


class Participant(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    age = models.CharField(max_length=2)
    linkedin_link = models.URLField()
    github_link = models.URLField()


class Enrollment(models.Model):
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    participantID = models.ForeignKey(Participant, on_delete=models.CASCADE, null=True)
