from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'ABHIGYAN'})

def pas(request):
    return HttpResponse("hii")

def password(request):
    lenght=int(request.GET.get('lenght'))
    upper_case = request.GET.get('uppercase')
    numeric_case = request.GET.get('numeric')
    special_case = request.GET.get('specialcase')
    # lenght=10
    pwd=''
    character=list('abcdefghijklmnopqrstuvwxyz')
    upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special = list('$%!@#&*()_+~|?><_')
    numeric = list('1234567890')
    if upper_case:
        character.extend(upper)
    if special_case:
        character.extend(special)
    if numeric_case:
        character.extend(numeric)

    for i in range(lenght):
        pwd = pwd + random.choice(character)
    return render(request,'generator/password.html',{'password':pwd})


