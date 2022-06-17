# Flights

Flights is a django web app for searching for flights provided in a csv file. 

It was written by Cameron Lanata for the ODS Full Stack interview take-home assignment. 

## Quick Start

To set up the environment for running the application, follow these steps (assumes Debian):

1. Create a virtualenv: `virtualenv -p /usr/bin/python3 env`
2. Activate the virtualenv: `python3 env/bin/activate`
3. Install the required packages: `pip install -r ods-coding-assignment/requirements.txt`
4. Set up the database: `python manage.py ods-coding-assignment/ods/manage.py`
5. Run pylint: `cd ods-coding-assignment; pylint flights ods --ignore=migrations`
6. Run unit tests: `python manage.py test flights`

Then, run the application with: `python ods-coding-assignment/ods/manage.py runserver`,
and see the running application in your browser at `http://localhost:8000/flights/`.

## Code Layout

The data schema is defined in flights/models.py.
The endpoint methods are defined in flights/views.py.
The endpoint urls are configured in flights/urls.py.
The UI is defined in flights/templates and flights/static.
