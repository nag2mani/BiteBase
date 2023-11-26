from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contest(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=1000)
    link = models.URLField()


class Job(models.Model):
    company_name = models.CharField(max_length=1000)
    skills = models.CharField(max_length=10000)
    posted_date = models.CharField(max_length=1000, null=True)
    apply_link = models.URLField()


class News(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    headline = models.CharField(max_length=1000)
    summary = models.CharField(max_length=10000000)
    link = models.URLField()


class Contact(models.Model):
    q_name = models.CharField(max_length=100)
    q_email = models.EmailField()
    q_subject = models.CharField(max_length=1000)
    q_message = models.CharField(max_length=10000000)