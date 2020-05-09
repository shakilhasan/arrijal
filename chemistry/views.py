from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages


def chemistry(request):
    template = loader.get_template('chemistry/animation.html')
    context = {}
    return HttpResponse(template.render(context, request))

def tankofnet(request):
    template = loader.get_template('chemistry/tankofnet.html')
    context = {}
    return HttpResponse(template.render(context, request))

def tank(request):
    template = loader.get_template('chemistry/tank.html')
    context = {}
    return HttpResponse(template.render(context, request))

def oxygen(request):
    template = loader.get_template('chemistry/oxygen.html')
    context = {}
    return HttpResponse(template.render(context, request))

def carbon(request):
    template = loader.get_template('chemistry/carbon.html')
    context = {}
    return HttpResponse(template.render(context, request))
