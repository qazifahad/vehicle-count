from django.shortcuts import render,HttpResponse
from .forms import *
# Create your views here.
def index(request):
    return render(request,'index.html')
