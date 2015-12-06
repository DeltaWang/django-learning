__author__ = 'apple'
# -*- coding: UTF-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context,Template
from books.models import Book
import datetime

def first_page(request):
    return HttpResponse('<p>hello,world!</p>')
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)


def current_datetime(request):
    current_date = datetime.datetime.now()+datetime.timedelta(hours=8)
    return render_to_response('current_date.html',locals())
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',locals())


