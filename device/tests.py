# from django.test import TestCase

# Create your tests here.
import pytest
from django.db.models import Avg
from .models import Terminal, Telemetry


@pytest.mark.django_db
def test_average_position_in_northern_hemisphere():
    # Seed data
    terminal1 = Terminal.objects.create(name='first_terminal')
    terminal2 = Terminal.objects.create(name='second_terminal')

    Telemetry.objects.create(
        terminal=terminal1,
        longitude=10.0,
        latitude=20.0
    )
    Telemetry.objects.create(
        terminal=terminal1,
        longitude=15.0,
        latitude=-30.0
    )
    Telemetry.objects.create(
        terminal=terminal2,
        longitude=5.0,
        latitude=40.0
    )

    # Perform the calculations
    terminals_with_avg_position = Terminal.objects.annotate(
        avg_longitude=Avg('terminal_telemetry__longitude'),
        avg_latitude=Avg('terminal_telemetry__latitude')
    )

    northern_hemisphere_average = terminals_with_avg_position.filter(avg_latitude__gte=0)

    # Check the result
    assert northern_hemisphere_average.count() == 1
    assert northern_hemisphere_average.first() == terminal2


