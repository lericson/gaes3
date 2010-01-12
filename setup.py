#!/usr/bin/env python
import os
from distutils.core import setup

readme_fn = os.path.join(os.path.dirname(__file__), "README.rst")
long_description = open(readme_fn, "U").read()

setup(name="gaes3", version="0.1", url="http://sendapatch.se/",
      author="Ludvig Ericson", author_email="ludvig@lericson.se",
      description="S3 interface for Google App Engine",
      long_description=long_description,
      py_modules=["gaes3"])
