from django.db import models
import uuid

# Create your models here.
class PersonalInfo(models.Model):

    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    location = models.CharField(max_length = 255)
    link = models.URLField()

    User = models.OneToOneField("User", on_delete = models.CASCADE, null = True, related_name="pinfo")

    def __str__(self):
        toFormat = "Name: {} {}\nEmail: {}\nPhone: {}\nLocation: {}\nLink: {}"
        return toFormat.format(self.firstName, self.lastName, self.email, self.phone, self.location, self.link)


class Education(models.Model):

    schoolName = models.CharField(max_length = 255)
    schoolLocation = models.CharField(max_length = 255)
    degree = models.CharField(max_length = 255)
    major = models.CharField(max_length = 255)
    gpa = models.CharField(max_length = 100 )
    startDate = models.CharField(max_length = 50)
    endDate = models.CharField(max_length = 50)
    #relevantCourses = models.TextField()
    User = models.ForeignKey("User", on_delete = models.CASCADE, null = True, related_name="edus")

    def __str__(self):
        toFormat = "Name: {}\nLocation: {}\nDegree: {}\nMajor: {}\nGPA: {}\nStart: {}\nEnd: {}"
        return toFormat.format(self.schoolName, self.schoolLocation, self.degree, self.major, self.gpa, self.startDate, self.endDate)


class WorkExperience(models.Model):

    companyName = models.CharField(max_length = 255)
    jobTitle = models.CharField(max_length = 255)
    companyLocation = models.CharField(max_length = 255)
    startDate = models.CharField(max_length = 50)
    endDate = models.CharField(max_length = 50)
    jobResp = models.TextField()
    User = models.ForeignKey("User", on_delete = models.CASCADE, null = True, related_name="experiences")

    def __str__(self):
        toFormat = "Name: {}\nJob Title: {}\nLocation: {}\nStart: {}\nEnd: {}\nResponsibilities: {}"
        return toFormat.format(self.companyName, self.jobTitle, self.companyLocation, self.startDate, self.endDate, self.jobResp)


class Project(models.Model):

    projectName = models.CharField(max_length = 255)
    projectDesc = models.TextField()
    link = models.URLField()
    tools = models.TextField()
    User = models.ForeignKey("User", on_delete=models.CASCADE, null = True, related_name="projects")

    def __str__(self):
        toFormat = "Name: {}\nDescription: {}\nLink: {}\nTools Used: {}"
        return toFormat.format(self.projectName, self.projectDesc, self.link, self.tools)


class User(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
