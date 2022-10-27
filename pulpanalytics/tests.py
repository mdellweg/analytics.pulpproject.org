from django.test import TestCase
from django.urls import reverse

from pulpanalytics.telemetry_pb2 import Telemetry

class ReceiveTelemetryTests(TestCase):
    def test_system_reports_twice(self):
        telemetry = Telemetry()
        telemetry.system_id = "00000000000000000000000000000000"
        response = self.client.post(reverse("pulpanalytics:index"), telemetry.SerializeToString(), "application/octets")
        assert response.status_code == 200, response.status_code
        response = self.client.post(reverse("pulpanalytics:index"), telemetry.SerializeToString(), "application/octets")
        assert response.status_code == 200, response.status_code
