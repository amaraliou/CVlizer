from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import uuid

#Personal Info Model with one to one relationship with the User Model
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


#Education Model with many to one relationship with the User Model
class Education(models.Model):

    schoolName = models.CharField(max_length = 255)
    schoolLocation = models.CharField(max_length = 255)
    degree = models.CharField(max_length = 255)
    major = models.CharField(max_length = 255)
    gpa = models.CharField(max_length = 100 )
    startDate = models.CharField(max_length = 50)
    endDate = models.CharField(max_length = 50)
    relevantCourses = models.TextField()
    User = models.ForeignKey("User", on_delete = models.CASCADE, null = True, related_name="edus")

    def __str__(self):
        toFormat = "Name: {}\nLocation: {}\nDegree: {}\nMajor: {}\nGPA: {}\nStart: {}\nEnd: {}\nRelevant Courses: {}"
        return toFormat.format(self.schoolName, self.schoolLocation, self.degree, self.major, self.gpa, self.startDate, self.endDate, self.relevantCourses)

'''
Example in models.py:

class Article(model.Models):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(User) #change this
    content = models.TextField()

Post Edit:

class Article(model.Models):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(settings.AUTH_USER_MODEL) #changed
    content = models.TextField()
'''

#Work Experience Model with many to one relationship with the User Model
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


#Project Model with many to one relationship with the User Model
class Project(models.Model):

    projectName = models.CharField(max_length = 255)
    projectDesc = models.TextField()
    link = models.URLField()
    tools = models.TextField()
    User = models.ForeignKey("User", on_delete=models.CASCADE, null = True, related_name="projects")

    def __str__(self):
        toFormat = "Name: {}\nDescription: {}\nLink: {}\nTools Used: {}"
        return toFormat.format(self.projectName, self.projectDesc, self.link, self.tools)


#User Model, every user can have one Personal Info submodel and several of the others
class User(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

#Remember to flush the database with python manage.py flush before using this.
'''
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, unique=True)
    alias = models.CharField(max_length=40)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS ["username", "alias"]

    def __str__(self):
        return "@{}".format(self.username)
    
    def get_short_name(self):
        return self.alias

    def get_long_name(self):
        return "{} @{}".format(self.alias, self.username)


class UserManager(BaseUserManager):

    def create_user(self, email, username, password, alias=None):
        if not email:
            raise ValueError("ENTER AN EMAIL BUDDY")
        if not username:
            raise ValueError("I KNOW YOU HAVE A NAME")
        if not password:
            raise ValueError("PASSWORD?!?!?!? HELLO??")
        if not alias:
            alias = username
        
        user = self.model(
             email = self.normalize_email(email),
             username = username,
             alias = alias)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, alias=None):
        user = self.create_user(email, username, password, alias)
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user
'''
#Skill Model with many to one relationship with the User Model
class Skill(models.Model):

    skillType = models.CharField(max_length = 255)
    skillList = models.TextField()
    User = models.ForeignKey("User", on_delete=models.CASCADE, null = True, related_name="skills")

    def __str__(self):
        toFormat = "Skill Name: {}\nSkill Details: {}"
        return toFormat.format(self.skillType, self.skillList)