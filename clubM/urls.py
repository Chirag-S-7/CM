from django.contrib import admin
from django.urls import path, include
from clubM import views
# from django.conf.urls import url

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.login, name='login'),
    path("about", views.about, name='about'),
    path("EventRegistration", views.EventRegistration, name='EventRegistration'),
    path("ParticipantRegistration", views.ParticipantRegistration, name='ParticipantRegistration'),
    path("EventDetails", views.EventDetails, name='EventDetails'),
    path("SignUp", views.SignUp, name='SignUp'),
    path("ParticipantList", views.ParticipantList, name='ParticipantList'),
    path("Clubs", views.Clubs, name='Clubs'),
    path("homeAdmin", views.homeAdmin, name='homeAdmin'),
    path("addClub", views.addClub, name='addClub'),
    path("addEvent", views.addEvent, name='addEvent'),
    path("addMember", views.addMember, name='addMember')
    # url(r'^pay/summary/(?P<value>\d+)/$', views.ParticipantList, name='ParticipantList'),
]