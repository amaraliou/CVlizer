from django.db import models

# Create your models here.
class PersonalInfo(models.Model):

    firstName = models.CharField(max_length = 255, null = False)
    lastName = models.CharField(max_length = 255, null = False)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    location = models.CharField(max_length = 255)
    link = models.URLField()

    def __str__(self):
        toFormat = "Name: {} {}\nEmail: {}\nPhone: {}\nLocation: {}\nLink: {}"
        return toFormat.format(self.firstName, self.lastName, self.email, self.phone, self.location, self.link)


class Education(models.Model):

    schoolName = models.CharField(max_length = 255, null = False)
    schoolLocation = models.CharField(max_length = 255, null = False)
    degree = models.CharField(max_length = 255, null = False)
    major = models.CharField(max_length = 255, null = False)
    gpa = models.CharField(max_length = 100)
    startDate = models.CharField(max_length = 50)
    endDate = models.CharField(max_length = 50)
    #relevantCourses = models.TextField()

    def __str__(self):
        return


class WorkExperience(models.Model):

    def __str__(self):
        return


class Skills(models.Model):

    def __str__(self):
        return


class Projects(models.Model):

    def __str__(self):
        return


class Extracurricular(models.Model):

    def __str__(self):
        return


class Resume(models.Model):

    def __str__(self):
        return