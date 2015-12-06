from django.shortcuts import render
# -*- coding: UTF-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context,Template
from books.models import Book
# Create your views here.

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 character')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
            {'books': books, 'query': q})

    return render_to_response('search_form.html',{'errors': errors})