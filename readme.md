# TELEMETRY ENGINE <!-- omit in toc -->


A repository for the calculation of telemetry data.

## Table of Contents <!-- omit in toc -->

- [Local Development](#local-development)


## Local Development

This section contains instructions on setting up the  stack on a local machine and manual setup.

#### Requirements

- Python
- django
- pytest-django

### Instructions:

1. Pull the [Telemetry Engine Repository](https://github.com/koiic/telemetry-engine) which includes the complete django stack existing in the directory
2. Navigate into the `telemetry_engine` directory.
3. Create a new virtual environment with `python3 -m venv venv`
4. Activate the virtual environment with `source .venv/bin/activate`
5. Install the dependencies with `pip install -r requirements.txt`
6. Run the migrations with  `python3 manage.py migrate`
7. Seed the database with `python3 manage.py shell < seed.py` (optional)
8. The application can also be tested by running `pytest`
9. To get terminals with average telemetry in northern hemisphere
       - `python3 manage.py shell`
       - ```python
         from device.models import Terminal, Telemetry
         from django.db.models import Avg
        
         avg_terminal_telemetry = Terminal.objects.annotate(
               avg_longitude=Avg('terminal_telemetry__longitude'),
               avg_latitude=Avg('terminal_telemetry__latitude')
           )
         northern_hemisphere_terminals = avg_terminal_telemetry.filter(avg_latitude__gte=0)
          
         print(f'Terminals in northern hemisphere: {northern_hemisphere_terminals}')
           ```