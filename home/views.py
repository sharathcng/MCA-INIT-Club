from django.shortcuts import render
from django.shortcuts import render,redirect,reverse


def home_page(request):
    return render(request,'home/homePage.html')
    
def faculty(request):
    return render(request,'home/faculty.html')

def publications(request):
    return render(request,'home/publications.html')

def committee(request):
    return render(request,'home/committee.html')