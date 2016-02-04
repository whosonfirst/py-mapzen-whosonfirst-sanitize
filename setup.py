#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.sanitize.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
version = open("VERSION").read()
desc = open("README.md").read()

setup(
    name='mapzen.whosonfirst.sanitize',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.sanitize'],
    version=version,
    description='Who\'s on First felpers for safely accepting user input',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-sanitize',
    install_requires=[
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-sanitize/releases/tag/' + version,
    license='BSD')
