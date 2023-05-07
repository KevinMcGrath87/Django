from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

# Create your views here.
def implication(request):
    return render(request,'logic_template.html')

def root(request):
    return redirect('/blog')

def blog(request,name="John Doe"):
    context = {
        'Name':f'{name}',
        'lastName': 'lastName',
        'text':'Well I got somin to sayyyyy!'
    }
    return render(request,'logic_template.html',context)

def new_blog(request):
    if request.method == "POST":
        return(redirect('/blog'))
    return HttpResponse("placeholder for a form to create a new blog")

def create(request):

    return redirect('/')

def number(request, number):
    return HttpResponse(f'placeholder text to display the number: {number}')


def edit(request, number):
    return HttpResponse(f'placeholder for editing the number {number}')

def json_response(request,name):
    print(request.path)
    print(request.method)
    return JsonResponse({f'{name}':'Is the coolest'})

def form(request):
    info = request.POST 
    return(redirect(f'/blog/{info["name"]}'))
