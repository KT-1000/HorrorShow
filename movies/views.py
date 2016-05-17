from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """ Takes in http request, renders the main page. """
    return HttpResponse("Horror movies best movies")
