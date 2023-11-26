from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout #login for storing session.
from django.contrib.auth.decorators import login_required
# Create your views here.

# def home(request):
#     return HttpResponse("""
# <h1> I am a Django Server</h1>
# <h2 style = "color:red" > I am working on good</h2>
# <p> I am a Django Server with some paragraph</p>
#    """)

# def contact(request):
#     return HttpResponse("""
# <h1> I am a Django Server of success page</h1>
# <h2 style = "color:blue" > I am working on success page </h2>
# <p> I am a Django Server with some paragraph</p>
#    """)



# peoples = [
#     {'name':'Nagmani', 'age':22},
#     {'name':'Nagu', 'age':21},
#     {'name':'Mani', 'age':12},
#     {'name':'Kajal', 'age':18},
#     {'name':'Dadu', 'age':20}
# ]


#for html templates.
def home(request):
    return render(request, 'index.html')

def contest(request):
    # contests_from_database = Contest.objects.all()   ##If you want to use all object.
    # contests_from_database = Contest.objects.all()[1:24]   ##If you want to object in some range.
    contests_from_database = Contest.objects.filter(Q(id__range=(1, 24)) | Q(id__range=(131, 206)))  # if we need multiple slices.
    return render(request, 'contest.html', context={'contest_list_all' : contests_from_database})


def job(request):
    jobs_from_database = Job.objects.all()
    return render(request, 'job.html', context={'job_list_all' : jobs_from_database})

@login_required(login_url="/login/")
def news(request):
    news_from_database = News.objects.all()[1:61]
    return render(request, 'news.html', context={'news_list_all' : news_from_database})


def contact(request):
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
            return redirect("/news/")

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect("/login/")


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



