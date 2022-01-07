# from django.http.response import JsonResponse
# from django.shortcuts import render
# from django.http import HttpResponse
import logging

# import json
# from django.http import JsonResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required


import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import *


logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return render(request, "bookings/index.html")


def book(request):
    return render(request, "bookings/book.html")


def change(request):
    return render(request, "bookings/change.html")


def services(request):
    services = Service.objects.all()
    logger.error(services)

    return JsonResponse([service.serialize() for service in services], safe=False)
