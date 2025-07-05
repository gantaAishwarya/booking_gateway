# Booking Gateway

## Overview

This service demonstrates integration with a mocked Property Management System (PMS) API. It fetches booking data, transforms it to an internal data model, and exposes the result through a clean Django REST endpoint.

## Features

- Fetch bookings from a mocked PMS API

- Map raw PMS data to the internal data structure

- Expose a REST API endpoint to serve transformed booking data

- Basic error handling for external API failures

- Unit tests covering the data mapping logic

## Installation & Setup

### Requirements

- Python
- Django
- Django REST Framework
- Docker

### Quick Start (with Docker)

####  Download docker

The easiest way to get up and running is with [Docker](https://www.docker.com/).

Just [install Docker](https://www.docker.com/get-started) and
[Docker Compose](https://docs.docker.com/compose/install/)

#### Clone the Git Repository and Navigate to the Project Directory

```bash
git clone https://github.com/gantaAishwarya/booking_gateway.git
cd booking_gateway
```

#### Start the Docker Containers

Run the following command in your terminal:

```bash 
docker-compose up
```
or 

```bash 
make start
```

This will start the PostgreSQL database, the web backend, and the mock PMS API, as well as apply any pending migrations.
Once everything is up and running, open your browser and visit [localhost:8000](http://localhost:8000/) to access the app.

#### Run Unit Tests for Data Mapping Logic

Execute the following command to run the unit tests for the data mapping logic:

```bash 
docker-compose exec web python manage.py test integrations.pms.tests.test_mapper
```
or
```bash
make test
```

*Note: If you encounter any errors, ensure that a .env file exists in your project directory. If not, create one by copying the provided .env.example file.*
