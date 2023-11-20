from django.shortcuts import render

# Create your views here.

def priya(request):
    return render(request,'priya.html')

def maa(request):
    return render(request,'maa.html')

def baba(request):
    return render(request,'baba.html')