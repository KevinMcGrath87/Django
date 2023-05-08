from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
import os
import random



def index(request):
    # upon a GET request we render the page and set the session values.
    # How can I get this initialization to happen only once?
    # if its not a GET request we render the page. //issue in that context is not necessarily defined when its a post
    flag = request.session['flag']
    if 'guessed' not in request.session:
        flag = False
        generated_number = random.randint(1, 10)
        request.session['generated_number']=generated_number
        print("flag is set to :" + str(flag))
    context = {
    'flag':flag,
    }
    print(flag)
    return(render(request,'index.html',context))


def reset(request):
    request.session['flag'] = False
    generated_number = random.randint(1,10)
    request.session['generated_number']=generated_number
    print("reset")
    return(redirect('/'))
# how does the guessed number get passed? Should be via request.POST[guessed_number]
def check_guess(request):
    guessed_number = int(request.POST['guessed_number'])
    generated_number = int(request.session['generated_number'])
    request.session['guessed']= True
    print(guessed_number)
    print(generated_number)
    if request.method == "GET":
        return(render(request,'index.html'))
    else:
        if generated_number==guessed_number:
            print("WINNER")
            request.session['flag']= 'equal'
            return(redirect('/'))
        elif generated_number <= guessed_number:
            print("high")
            request.session['flag']= 'high'
            return(redirect('/'))
        else:
            print("low")
            request.session['flag']='low'
            return(redirect('/'))

        

# def check_guess(request, guessed_number):
#     flag=request.session['flag']
#     if request.method == "POST":
#         guessed_number= request.POST['guessed_number']
#         if int(guessed_number) == generated_number:
#             flag = True
#     else: 
#         flag = False

#     return(redirect('/'))



