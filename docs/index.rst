.. django-profiletools documentation master file, created by
   sphinx-quickstart on Thu Aug  9 06:38:45 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-profiletools's documentation!
===============================================

Contents:

.. toctree::
   :maxdepth: 2

About
------

I got tired of cutting and pasting these components from one project to another. So I released django-profiletools.

The lazy loading of profiles was inspired by the rather incredible Noah Kantrowitz.

Features
------------

* Lazy loading of your authenticated `profile` record across the `request` object lifetime. That means in the Python code and the templates.
* Name your profile model anything you want in `settings.AUTH_PROFILE_MODULE`.

Installation
------------

Get the code::

	pip install django-profiletools

Install the middleware and context_processor in your settings.py::

	TEMPLATE_CONTEXT_PROCESSORS = (
		...
	    'profiletools.context_processors.fetch_profile',
	)

	MIDDLEWARE_CLASSES = (
	...
	'profiletools.middleware.LazyProfileMiddleware',
	)

Also in settings.py, set the AUTH_PROFILE_MODULE to your profile model::

	AUTH_PROFILE_MODULE = "profiles.Profile"

Based on that, your profile model should resemble something like::

	# profiles.models.Profile.py
	from django.contrib.auth.models import User
	from django.db import models

	class Profile(models.Model):

	    user = models.OneToOneField(User)
	    
	    def __unicode__(self):
	        return self.user.username






Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

