#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# To register app to PyPI:
# python setup.py register -r pypi
#
# NOTE: To update PyPI, tag the current release:
#
# First increment cache_tools/__init__.py
# Then:
# > git tag x.y.z -m "Version bump for PyPI"
# > git push --tags origin master
# Then:
# > python setup.py sdist upload
#

from setuptools import setup, find_packages
from aldryn_newsblog_extra_plugins import __version__


INSTALL_REQUIRES = [
    'aldryn-newsblog',
    'six',
]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python',
]

setup(
    name='aldryn-newsblog-extra-plugins',
    version=__version__,
    description='Extra plugins for aldryn-newsblog.',
    author='Fabian Lehner',
    author_email='fabian.lehner@marmara.at',
    url='https://github.com/febsn/aldryn-newsblog-extra-plugins',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    license='MIT',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
)
