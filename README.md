# django_quoteoftheday
A Django App that inserts random quotes into your page (Hand curated)

# Installation

Clone this repository and place the ```qotd``` directory in your Django Project. 

Enable the app by adding it to your ```INSTALLED_APPS``` list in your project's settings like so:

```python
INSTALLED_APPS = [
	...,
	'qotd'
	...,
]
``` 

Afterwars, run ```python manage.py makemigrations``` to create all necessary migrations and ```python manage.py migrate``` to apply them to your database.

# Usage

## Datamodel

Quote are usually attributed to a person (or organization). This relationship is implemented in this app through a foreign key relationship. Each quote is attributed to an attributee, both of which have to be created in the backend. Naturally, the attributee has to be created first, so that one or more quotes can be attributed to them.

Each attributee can have a biography linked to them via a URL, as well as an authority-record.

Each quote consists of an attributee (foreign key), the quote itself as well as a source. The source needs to be given as text, and can have a link attached to it, to reference the source.

## In a template

This app provides a simple template tag to render a quote at the position of the tag. In a template you insert a quote like so:

```Jinja2
{% load qotd_tags %}

<html>
	<head>
	...
	</head>

	<body>
		...
		{% qotd %}
		...
	</body>
</html>
```

This will render a quote according to the template provided in ```qotd/templates/quote.html```. This template requires Bootstrap 5, so change it if you need something else.

## The "of the day" part

This app provides a random quote each time the page is loaded. This happens by using Python's random library. Since the random number generator is seeded with the current server time, calling the same page in less than a few seconds will result in the same quote, since the random number generator will always produce the same sequence with the same seed. 

While this isn't strictly a "quote of the day" it can easily be made into one, by producing a random number once a day and storing it somewhere in a cache.

# Wagtail CMS integration
This app provides a ```wagtail_hooks.py``` to facilitate integration into a Wagtail CMS. Delete it if you're not using Wagtail CMS to avoid errors.

# Environment

This app is tested on:
- Python 3.8, 3.9, 3.10
- Django 3.1, 3.2
- Wagtail 2.14, 2.15