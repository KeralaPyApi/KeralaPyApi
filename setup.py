#!/usr/bin/env python
from setuptools import setup
from io import open

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

setup(name='KeralaPyApi',
      version='1.0.2',
      description='Telegram bot api using Python. ',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      author='Mario',
      author_email='keralapyapi@gmail.com',
      url='https://github.com/KeralaPyApi/KeralaPyApi',
      packages=['keralabot'],
      license='GPLv2',
      keywords='telegram bot api using python',
      install_requires=['requests', 'six'],
      extras_require={
          'json': 'ujson',
      },
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
