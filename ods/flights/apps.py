"The django app configuration for the flights app"
from django.apps import AppConfig


class FlightsConfig(AppConfig):
    "Define the flights app configuration"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flights'
