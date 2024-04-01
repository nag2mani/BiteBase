from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout #login for storing session.
from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay
import requests


def home(request):
    return render(request, 'index.html')


@login_required(login_url="/login/")
def contest(request):
    # contests_from_database = Contest.objects.all()   ##If you want to use all object.
    # contests_from_database = Contest.objects.all()[1:24]   ##If you want to object in some range.
    contests_from_database = Contest.objects.filter(Q(id__range=(1, 24)) | Q(id__range=(131, 206)))  # if we need multiple slices.
    return render(request, 'contest.html', context={'contest_list_all' : contests_from_database})


@login_required(login_url="/login/")
def job(request):
    jobs_from_database = Job.objects.all()
    return render(request, 'job.html', context={'job_list_all' : jobs_from_database})


@login_required(login_url="/login/")
def news(request):
    news_obj = User.objects.filter(username = 'username')

    # When you use razorpay API key then uncomment these three lines as well as keep context line which have payments.
    client = razorpay.Client(auth = (settings.KEY_ID, settings.SECRET_KEY))
    payment = client.order.create({'amount' :100, 'currency':'INR', 'payment_capture':1})
    news_obj.razor_pay_order_id = payment['id']

    news_from_database = News.objects.all()[101:161]
    ## ads_news = Add_your_news.objects.all().order_by('-pk').first()  #to find latest insertiond
    ads_news = Add_your_news.objects.all()[1]

    context={'news_list_all' : news_from_database, 'ads_news' : ads_news, 'payment' : payment}
    return render(request, 'news.html', context)


def contact(request):
    if request.method == "POST":
        q_name = request.POST.get('q_name')
        q_email = request.POST.get('q_email')
        q_subject = request.POST.get('q_subject')
        q_message = request.POST.get('q_message')

        Contact.objects.create(
            q_name = q_name,
            q_email = q_email,
            q_subject = q_subject,
            q_message = q_message
            )
        
        messages.info(request, "Your Query Accepted, We will get back to you sortly.")
        return redirect("/contact/")
    
    return render(request, 'contact.html')



def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username")
            return redirect("/login/")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect("/login/") 
        else:
            login(request, user)
            return redirect("/")

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect("/")


def signup(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken")
            # messages.warning(request, "Username already taken")
            return redirect("/signup/")

        else:
            User.objects.create_user(
                first_name = first_name,
                email = email,
                username = username,
                password=password
            )
            messages.info(request, "Account Created Successfully")
            return redirect("/signup/")

    return render(request, 'signup.html')


# def payment_required(view_func):
#     # This will help us to not access ads page before payments.
#     def _wrapped_view(request, *args, **kwargs):
#         # Verify payment status using Razorpay API
#         user_profile = UserProfile.objects.get(user=request.user)
#         if user_profile.has_paid:
#             return view_func(request, *args, **kwargs)
#         else:
#             messages.error(request, "You need to make a payment to access this page.")
#             return redirect("payment_page")  # Redirect to the payment page or any other page
#     return _wrapped_view



@login_required(login_url="/login/")
# @payment_required  # Apply the payment check decorator
def add_your_news(request):
    if request.method == "POST":
        headline = request.POST.get('headline')
        link = request.POST.get('link')
        summary = request.POST.get('summary')
        image = request.FILES.get('image')

        Add_your_news.objects.create(
            headline = headline,
            link = link,
            summary = summary,
            image = image
            )
        
        messages.info(request, "Congratulations! Your news added.")
        return redirect("/add_your_news/")

    return render(request, 'add_your_news.html')



