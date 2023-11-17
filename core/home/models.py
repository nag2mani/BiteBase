from django.db import models
# Create your models here.

class Contest(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=1000)
    link = models.URLField()




