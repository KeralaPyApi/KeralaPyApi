#!/usr/bin/env python
from setuptools import setup, find_packages
from io import open
import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


packages = find_packages(exclude=['logos*'])


setup(name='KeralaPyApi',
      version='0.3.0',
      description='Python Telegram bot api. ',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Kerala Team',
      author_email='anandvfc640@gmail.com',
      url='https://github.com/KeralaPyApi/KeralaPyApi.git',
      packages=packages,
      license='GPLv2',
      keywords='telegram bot api tools',
      install_requires=requirements(),
      extras_require={
          'json': 'ujson',
      },
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
      ]
      )
