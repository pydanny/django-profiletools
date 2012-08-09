from setuptools import setup, find_packages

import profiletools

LONG_DESCRIPTION = open('README.rst').read()

setup(
    name='django-profiletools',
    version=profiletools.__version__,
    description="Tools for Profile models in Django.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='django,profiles',
    author=profiletools.__author__,
    author_email='pydanny@gmail.com',
    url='http://github.com/pydanny/django-profiletools',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
)