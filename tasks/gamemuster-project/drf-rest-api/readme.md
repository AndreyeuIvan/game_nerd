# Create REST API using DRF

## Short Description

Store games in Database.

## Estimation (h)

56

## Topics

* Python/Django
* Django models
* Django management commands
* Celery

## Requirements

Store games in Database, refresh periodically using Celery or using [Django management commands](https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)

* Create game model
* Implement python script for downloading games form IGDB API to app&#39;s db (Django manage command)
* Create Django Celery task for downloading games on a regular basis
