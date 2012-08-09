.. django-profiletools documentation master file, created by
   sphinx-quickstart on Thu Aug  9 06:38:45 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-profiletools's documentation!
===============================================

Where is the source code?
-------------------------

https://github.com/pydanny/django-profiletools


About
------

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

.. note:: If you don't use ``profiles.models.Profile``, say ``members.models.UserProfile`` go ahead and change the ``AUTH_PROFILE_MODULE`` to "members.UserProfile".

Usage
------

In your templates::

	{{ request.my_profile }}

In your functional views::

	profile = request.my_profile

In your class-based views::

	profile = self.request.my_profile	

Call my_profile as many times as you want, it only loads once. So if you call it 100 times in a view, the ``SQL SELECT`` is only done the first time. If no user is found then the my_profile call result is ``None``, which makes it easier to handle templates which need to be able to handle unauthenticated users (like the `about` page).

.. note:: If you are using the ``members.UserProfile`` example, you'll need to call that by using ``request.my_userprofile``.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

