"The unit tests for the flights app"
from django.test import TestCase
from django.utils import timezone
from .models import Flight
from .views import _search_origin, _search_destination

class FlightsTestCase(TestCase): # pylint: disable=no-member
    "Unit tests for the main functionality"

    def setUp(self):
        "Create Flight objects for testing"
        Flight.objects.create(
            flight_id="123456",
            created_at=timezone.now(),
            updated_at=timezone.now(),
            flight_identifier = "abcede-12345",
            flt_num = "1234",
            scheduled_origin_gate="001",
            scheduled_destination_gate="Any",
            out_gmt = timezone.now(),
            in_gmt = timezone.now(),
            off_gmt = timezone.now(),
            on_gmt = timezone.now(),
            destination = "ATL",
            origin="BNA",
            destination_full_name="Atlanta",
            origin_full_name="Nashville"
        )
        Flight.objects.create(
            flight_id="654321",
            created_at=timezone.now(),
            updated_at=timezone.now(),
            flight_identifier = "fghijk-45678",
            flt_num = "4567",
            scheduled_origin_gate="002",
            scheduled_destination_gate="Any",
            out_gmt = timezone.now(),
            in_gmt = timezone.now(),
            off_gmt = timezone.now(),
            on_gmt = timezone.now(),
            destination = "DEN",
            origin="TPA",
            destination_full_name="Denver",
            origin_full_name="Tampa"
        )

    def test_search_origin(self):
        "Test that search_origin returns flights matching the search"
        bna_flight = Flight.objects.get(flight_id="123456")
        tpa_flight = Flight.objects.get(flight_id="654321")
        self.assertIn(bna_flight, _search_origin("bna"))
        self.assertIn(tpa_flight, _search_origin("tpa"))
        self.assertNotIn(bna_flight, _search_origin("tpa"))
        self.assertNotIn(tpa_flight, _search_origin("bna"))

    def test_search_destination(self):
        "Test that search_origin returns flights matching the search"
        atl_flight = Flight.objects.get(flight_id="123456")
        den_flight = Flight.objects.get(flight_id="654321")
        self.assertIn(atl_flight, _search_destination("atl"))
        self.assertIn(den_flight, _search_destination("den"))
        self.assertNotIn(atl_flight, _search_destination("den"))
        self.assertNotIn(den_flight, _search_destination("atl"))
