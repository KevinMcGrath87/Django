from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from time import strftime, gmtime

# Create your views here.
def display_time(request):
    context={
        'time':strftime("%Y-%m-%d %H:%M %p",gmtime())
    }

    return render(request, 'display_time.html',context)