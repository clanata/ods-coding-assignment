"Define endpoint methods for flights app"
from django.db.models import Q
from django.forms import ModelForm
from django.views import generic, View
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.core.exceptions import ValidationError
from django.forms.widgets import TextInput
from .models import Flight

class FlightResultsView(generic.ListView):
    "View for list of flights searched by origin"

    model = Flight
    allow_empty = True

    def get_queryset(self):
        """Return queryset of flights that match search"""
        origin = self.kwargs.get('origin', None)
        destination = self.kwargs.get('destination', None)
        if origin and destination:
            return _search_origin(origin) & _search_destination(destination)
        if origin:
            return _search_origin(origin)
        if destination:
            return _search_destination(destination)
        return Flight.objects.all() # pylint: disable=no-member

class FlightSearchForm(ModelForm): # pylint: disable=too-few-public-methods
    "Form definition for searching flights"

    class Meta: # pylint: disable=too-few-public-methods
        "Define attributes of form"
        model = Flight
        fields = ['destination_full_name', 'origin_full_name']
        widgets = {
            'destination_full_name': TextInput(attrs={'list': 'stations'}),
            'origin_full_name': TextInput(attrs={'list': 'stations'}),
        }

    def clean(self):
        "Validate either origin, destination, or both"
        super().clean()
        origin = self.cleaned_data.get("origin_full_name", None)
        destination = self.cleaned_data.get("destination_full_name", None)
        if not origin and not destination:
            raise ValidationError("Please specify either origin or destination.")

class FlightSearchView(View):
    "View that returns form for searching flights"

    def get(self, request):
        "Return the form"
        form = FlightSearchForm()
        return render(request, "flights/search.html", {"form": form})

    def post(self, request):
        "Redirect to the search results"
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            origin = form.cleaned_data.get("origin_full_name", None)
            destination = form.cleaned_data.get("destination_full_name", None)
            if origin and destination:
                redirect = f"flights/{origin}/{destination}/"
            if origin:
                redirect = f"origins/{origin}/"
            if destination:
                redirect = f"destinations/{destination}/"
            return HttpResponseRedirect(redirect)
        return render(request, "flights/search.html", {"form": form})

class FlightSuggestionsView(View):
    "View to handle auto-suggestions feature"

    def get(self, _request, search=None):
        "Return station suggestions in JSON format"
        stations = []
        if len(search) > 1:
            stations = list(_auto_suggest(search))
        return JsonResponse({"stations": stations})

def _search_origin(search_term):
    "Return flights with origin that match search term"
    return Flight.objects.filter( # pylint: disable=no-member
        Q(origin__icontains=search_term) |
        Q(origin_full_name__icontains=search_term)
    )

def _search_destination(search_term):
    "Return flights with destination that matches search term"
    return Flight.objects.filter( # pylint: disable=no-member
        Q(destination__icontains=search_term) |
        Q(destination_full_name__icontains=search_term)
    )

def _auto_suggest(search_term):
    "Return suggestions for stations from search term"
    origins = set(flight.origin_station() for flight in _search_origin(search_term))
    destinations = set(flight.destination_station() for flight in _search_destination(search_term))
    stations = origins | destinations
    return stations
