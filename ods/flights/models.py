"Define the data schema for the flights app"
from django.db import models


class Flight(models.Model):
    "A table for flight data"

    flight_id = models.CharField("ID", max_length=6)
    created_at = models.DateTimeField("Created")
    updated_at = models.DateTimeField("Updated")
    flight_identifier = models.CharField("Flight Identifier", max_length=36)
    flt_num = models.CharField("Flight Number", max_length=4)
    scheduled_origin_gate = models.CharField("Origin Gate", max_length=3)
    scheduled_destination_gate = models.CharField("Destination Gate", max_length=3)
    out_gmt = models.DateTimeField("Departure")
    in_gmt = models.DateTimeField("Arrival")
    off_gmt = models.DateTimeField("Take-Off")
    on_gmt = models.DateTimeField("Landing")
    destination = models.CharField("Destination Code", max_length=3)
    origin = models.CharField("Origin Code", max_length=3)
    destination_full_name = models.CharField("Destination", max_length=64, blank=True, null=True)
    origin_full_name = models.CharField("Origin", max_length=64, blank=True, null=True)


    def destination_station(self):
        "Return the destination name and station code"

        return f"{self.destination_full_name} ({self.destination})"

    def origin_station(self):
        "Return the origin name and station code"

        return f"{self.origin_full_name} ({self.origin})"
