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


# this is where I will write code for the counter part of the assighment.
def counter(request):
    if 'count' in request.session:
        count = request.session['count']
        count += 1
        request.session['count']=count
        return(redirect('/counter_display'))
    else:
        request.session['count'] = 1;
        return(redirect('/counter_display'))

def counter_display(request):
    context = {
        'count': request.session['count'],
    }
    return(render(request,'counter_display.html',context))
