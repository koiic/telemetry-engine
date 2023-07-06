from device.models import Terminal, Telemetry


def seed_data():
    # Create Terminal instances
    first_terminal = Terminal.objects.create(name='first_terminal', is_active=True)
    second_terminal = Terminal.objects.create(name='second_terminal', is_active=False)

    # Create Telemetry instances
    Telemetry.objects.create(terminal=first_terminal, longitude=11.123456, latitude=22.654321)
    Telemetry.objects.create(terminal=first_terminal, longitude=18.987654, latitude=75.123456)
    Telemetry.objects.create(terminal=second_terminal, longitude=5.432109, latitude=40.678901)


seed_data()