from django.shortcuts import render

# Create your views here.
from  django.http import HttpResponse
def first_page(request):
    return HttpResponse('<p>how to get away with murder</p>')