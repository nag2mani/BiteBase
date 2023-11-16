from django.shortcuts import render
from django.http import HttpResponse

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


peoples = [
    {'name':'Nagmani', 'age':22},
    {'name':'Nagu', 'age':21},
    {'name':'Mani', 'age':12},
    {'name':'Kajal', 'age':18},
    {'name':'Dadu', 'age':20}
]

text = """Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eos ipsa rerum error corrupti vel, maiores laboriosam aliquid eligendi quidem reiciendis alias natus sunt id deserunt vitae ducimus veritatis modi? Quas, amet impedit. Fugit, facere? Tempora aliquam nesciunt reprehenderit totam exercitationem assumenda laborum neque. Blanditiis perfer"""

# for people in peoples:
#     print(people['name'])

#for html templates.
def home(request):
    return render(request, 'contest.html', context={'my_dict': peoples, 'text':text})


def contact(request):
    context = {'page': 'contact'}
    return render(request, 'contact.html', context)

def service(request):
    context = {'page': 'service'}
    return render(request, 'service.html', context)




