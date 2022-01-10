from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book", views.book, name="book"),
    path("cancel", views.cancel, name="cancel"),
    path("services", views.services, name="services"),
    path("dates", views.dates, name="dates"),
]
