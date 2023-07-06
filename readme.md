# TELEMETRY ENGINE <!-- omit in toc -->

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

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
6. create a new virtual environment with `python3 -m venv venv`
7. activate the virtual environment with `source .venv/bin/activate`
8. install the dependencies with `pip install -r requirements.txt`
9. run the migrations with `python3 manage.py makemigrations` and `python3 manage.py migrate`
10. Seed the database with `python3 manage.py shell < seed.py` (optional)
11. Or you can test the application with `pytest`
    10. To get terminals with average telemetry in northern hemisphere
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

7

