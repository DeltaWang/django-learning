# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context,Template
from django.core.mail import send_mail
from contact.forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
def emailsuccess(request):
    return render_to_response('emailsuccess.html')
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_date
#             send_mail(
#                 cd['subject'],
#                 cd['message'],
#                 cd.get('email','noreply@eample.com'),
#                 ['plunk777@163.com'],
#
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#
#     else:
#         form = ContactForm()
#     return render_to_response('contact_form.html',{'form':form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})