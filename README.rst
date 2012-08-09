===================
django-profiletools
===================
:Info: Tools for Profile models in Django.
:Version: 0.1.0
:Author: Daniel Greenfeld (http://pydanny.com)

About
=====

I got tired of cutting and pasting these components from one project to another. So I released django-profiletools.

The lazy loading of profiles was inspired by the rather incredible Noah Kantrowitz.

Features
========

* Lazy loading of your authenticated `profile` record across the `request` object lifetime. That means in the Python code and the templates.
* Name your profile model anything you want in `settings.AUTH_PROFILE_MODULE`.

Installation
============

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

.. note:: If you don't use profiles.models.Profile, say members.models.Member go ahead and change the AUTH_PROFILE_MODULE to "members.Member".

Usage
------

In your templates::

	{{ request.my_profile }}

In your functional views::

	profile = request.my_profile

In your class-based views::

	profile = self.request.my_profile	

Call my_profile as many times as you want, it only loads once. So if you call it 100 times in a view, the ``SQL SELECT`` is only done the first time.

.. note:: If you are using the ``members.Member'``example, you'll need to call that by using ``request.my_member``.