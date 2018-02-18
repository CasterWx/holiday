# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from message.models import UserMessage
# Create your views here.
def getform(request): 
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        message = request.POST.get('message','')
        mess = UserMessage()
        mess.name = name
        mess.email = email
        mess.adress = address
        mess.message = message
        mess.save()
    return render(request, 'message_form.html')

