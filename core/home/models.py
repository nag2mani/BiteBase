from django.db import models
from django.contrib.auth.models import User


# These are my models, created for database.

class Contest(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=1000)
    link = models.URLField()


class Job(models.Model):
    company_name = models.CharField(max_length=1000)
    skills = models.CharField(max_length=10000)
    posted_date = models.CharField(max_length=1000, null=True)
    apply_link = models.URLField()


# class UserProfile(models.Model):
#     # This is for not accessing the adding news page without payments.
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add additional fields as needed.

#     def __str__(self):
#         return self.user.username

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


class News(models.Model):
    # If with news we can also add like and dislike button so that users can validae the machine learning model.
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)

    razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_patment_signature = models.CharField(max_length=100, null=True, blank=True)

    headline = models.CharField(max_length=1000)
    summary = models.CharField(max_length=10000000)
    link = models.URLField()
    percent = models.IntegerField()


class Contact(models.Model):
    q_name = models.CharField(max_length=100)
    q_email = models.EmailField()
    q_subject = models.CharField(max_length=1000)
    q_message = models.CharField(max_length=10000000)


class Add_your_news(models.Model):
        headline = models.CharField(max_length=1000)
        link = models.URLField()
        summary = models.CharField(max_length=10000000)
        image = models.ImageField(upload_to="ads_image")