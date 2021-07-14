from django.http.response import HttpResponseGone
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, localtime, strftime 
# Create your views here.



def index(request):
    return redirect("/palabra_random")
def wordRandom(request):
    palabra = get_random_string(length=14)
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return render(request,'index.html',{"word":palabra})
def reset(request):
    request.session.clear()
    return redirect("/palabra_random")
    