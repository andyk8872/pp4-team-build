from . import views
from django.urls import path


urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("make_booking/", views.make_booking, name="make_booking"),
]
