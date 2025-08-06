from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about_us", views.about_us, name="about_us"),
    path("our_brands", views.our_brands, name="our_brands"),
    path("our_channel", views.our_channel, name="our_channel"),
    path("connect_us", views.connect_us, name="connect_us"),
    path("brand_details", views.brand_details, name="brand_details"),
]

