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
* Prebuilt views and forms to go along with your custom profile model.

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

Forms and views
---------------

``profiletools.forms.ProfileForm`` and the views in ``profiletools.views``
use the model named by ``AUTH_PROFILE_MODULE``. They resolve that model when
their modules are imported. Configure the setting and make the model available
before importing the forms or views.

These examples use the project's legacy Django APIs, including
``AUTH_PROFILE_MODULE``. They are not instructions for migrating to a current
Django release.

Choosing editable fields
~~~~~~~~~~~~~~~~~~~~~~~

``ProfileForm`` is a ``ModelForm`` whose ``Meta`` options come from attributes
on the profile model:

* ``model`` is the model resolved from ``AUTH_PROFILE_MODULE``.
* ``fields`` is the model's ``fields`` attribute, or ``()`` if it is absent.
* ``exclude`` is the model's ``exclude`` attribute, or ``('user',)`` if it is
  absent.

Set an explicit allowlist of editable fields on your model. For example, a
profile with an editable biography can be defined as follows::

    from django.contrib.auth.models import User
    from django.db import models

    class Profile(models.Model):
        user = models.OneToOneField(User)
        bio = models.TextField(blank=True)

        fields = ('bio',)
        exclude = ('user',)

Use the application's normal schema-management process if adding fields to an
existing model. Keep the ``user`` relationship out of the editable fields, as
shown above, so the form edits profile content rather than its owner.

Choosing a view
~~~~~~~~~~~~~~~

All six views use the configured profile model. The update views use
``ProfileForm``.

* ``ProfileDetailView`` extends Django's ``DetailView`` and includes
  ``django-braces``' ``LoginRequiredMixin``. It uses the generic view's
  primary-key or slug lookup.
* ``ProfileUpdateView`` extends ``UpdateView`` and includes
  ``LoginRequiredMixin``. It also uses the generic view's primary-key or slug
  lookup.
* ``ProfileUpdateNoSlugView`` extends ``ProfileUpdateView`` and replaces the
  lookup with ``PROFILE_MODEL.objects.get(user=self.request.user)``. It needs
  no profile identifier in the URL, but requires that the user's profile
  already exists. It does not catch the model's ``DoesNotExist`` exception.
* ``DefaultProfileUpdateNoSlugView`` extends ``ProfileUpdateView`` and uses
  ``get_or_create(user=self.request.user)`` instead. It can create a profile
  while fetching the object, including when displaying the edit page. Any
  other required model fields must support creation without additional
  arguments.
* ``ProfileListView`` extends ``ListView`` without a login mixin of its own.
* ``LoginRequireProfileListView`` extends ``ListView`` with
  ``LoginRequiredMixin``. Note the exact class name: ``LoginRequire``, not
  ``LoginRequired``.

Use one of the no-slug update views for an edit page that selects the signed-in
user's profile. The detail, list and ordinary update views use Django's generic
object selection instead. Configure the application's queryset and permission
policy when using those views; a login requirement alone does not select the
current user's profile.

Editing an existing profile
~~~~~~~~~~~~~~~~~~~~~~~~~~

For a project that creates each user's profile before it can be edited, add
an edit route using ``ProfileUpdateNoSlugView``. This legacy URLconf example
sets both the template and the redirect after a successful update explicitly::

    from django.conf.urls import patterns, url
    from profiletools.views import ProfileUpdateNoSlugView

    urlpatterns = patterns('',
        url(r'^profile/edit/$',
            ProfileUpdateNoSlugView.as_view(
                template_name='profiles/profile_form.html',
                success_url='/',
            ),
            name='profile_update'),
    )

Create ``profiles/profile_form.html`` in the application's template directory::

    <form method="post" action="">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save profile</button>
    </form>

Choose a suitable ``success_url`` and retain the application's normal CSRF
protection. If a profile may be missing, decide whether to create it elsewhere
or deliberately use ``DefaultProfileUpdateNoSlugView`` with the creation
behavior described above. Neither current-user view takes a ``pk`` or
``slug`` argument in its ``get_object`` method.

Problems with Python's "**is**" evaluation and "**type**" built-in
==================================================================

If you use the **is** evaluation before doing anything else with the my_profile object, it will behave in a slightly unexpected manner:

The  **will always return false**. For example::

    >>> print(request.my_profile is None)
    False
    >>> p = request.user.get_profile()
    >>> print(request.my_profile is p)
    False
    
    
Also, the **type** built-in will return a ``django.utils.functional.SimpleLazyObject`` object::

    >>> print(type)
    <class 'django.utils.functional.SimpleLazyObject'>

Keep in mind what is placed in the ``my_profile`` value is not a ``ModelClass``
instance or ``None`` object, but rather a ``django.utils.functional.SimpleLazyObject``.

**How to evaluate the my_profile object**

Use ``==`` to evaluate the my_profile object. This forces the object to be evaluated
and won't return frustrating false-positives.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

