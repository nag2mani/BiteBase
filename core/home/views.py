from django.shortcuts import render
from django.http import HttpResponse
from home.models import *
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
    contests_from_database = Contest.objects.all()
    return render(request, 'contest.html', context={'contest_list_all' : contests_from_database})


def job(request):
    return render(request, 'job.html')


def news(request):
    return render(request, 'news.html')




