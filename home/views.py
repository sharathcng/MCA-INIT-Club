from django.shortcuts import render
from django.shortcuts import render,redirect,reverse


def home_page(request):
    return render(request,'home/homePage.html')
    
def faculty(request):
    return render(request,'home/faculty.html')