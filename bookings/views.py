import logging
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import datetime


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
    return JsonResponse([service.serialize() for service in services], safe=False)


def dates(request):
    # generate rows for next 30 days
    # get today date
    today = datetime.date.today()
    enddate = today + datetime.timedelta(days=29)

    # loop 30 times and check if row exists in db
    # TODO filter to show only future
    for x in range(30):
        date = today + datetime.timedelta(days=x)

        # if not create empty row with correct date
        if not Day.objects.filter(date=date).exists():
            day = Day(date=date)
            day.save()

    # output all future and today objects
    days = Day.objects.filter(date__range=[today, enddate]).order_by("date")

    # prepare JSON response

    return JsonResponse([day.serialize() for day in days], safe=False)
