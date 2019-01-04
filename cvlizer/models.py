from django.db import models

# Create your models here.
class PersonalInfo(models.Model):

    firstName = models.CharField(max_length = 255, default = "BRUH")
    lastName = models.CharField(max_length = 255, default = "BRUH")
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    location = models.CharField(max_length = 255)
    link = models.URLField()

    Resume = models.OneToOneField("Resume", on_delete = models.CASCADE, null = True, related_name="pinfo")

    def __str__(self):
        toFormat = "Name: {} {}\nEmail: {}\nPhone: {}\nLocation: {}\nLink: {}"
        return toFormat.format(self.firstName, self.lastName, self.email, self.phone, self.location, self.link)


class Education(models.Model):

    schoolName = models.CharField(max_length = 255, default = "BRUH")
    schoolLocation = models.CharField(max_length = 255, default = "BRUH")
    degree = models.CharField(max_length = 255, default = "BRUH")
    major = models.CharField(max_length = 255, default = "BRUH")
    gpa = models.CharField(max_length = 100, default = "BRUH" )
    startDate = models.CharField(max_length = 50, default = "BRUH")
    endDate = models.CharField(max_length = 50, default = "BRUH")
    #relevantCourses = models.TextField()

    Resume = models.ForeignKey("Resume", on_delete = models.CASCADE, null = True, related_name="edus")

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

    Resume = models.ForeignKey("Resume", on_delete = models.CASCADE, null = True, related_name="experiences")

    def __str__(self):
        toFormat = "Name: {}\nJob Title: {}\nLocation: {}\nStart: {}\nEnd: {}\nResponsibilities: {}"
        return toFormat.format(self.companyName, self.jobTitle, self.companyLocation, self.startDate, self.endDate, self.jobResp)


class Project(models.Model):

    projectName = models.CharField(max_length = 255)
    projectDesc = models.TextField()
    link = models.URLField()
    tools = models.TextField()
    Resume = models.ForeignKey("Resume", on_delete=models.CASCADE, null = True, related_name="projects")

    def __str__(self):
        toFormat = "Name: {}\nDescription: {}\nLink: {}\nTools Used: {}"
        return toFormat.format(self.projectName, self.projectDesc, self.link, self.tools)


class Resume(models.Model):

    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
