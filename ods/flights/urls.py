"""Flights URL Configuration"""
from django.urls import path

from . import views

app_name = 'flights' # pylint: disable=invalid-name
urlpatterns = [
    path('', views.FlightSearchView.as_view()),
    path('origins/<origin>/', views.FlightResultsView.as_view()),
    path('destinations/<destination>/', views.FlightResultsView.as_view()),
    path('flights/<origin>/<destination>/', views.FlightResultsView.as_view()),
    path('stations/<search>/', views.FlightSuggestionsView.as_view()),
]
