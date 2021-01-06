# coding: utf-8

from setuptools import setup, find_packages

    
setup(
    name='cloudwatch_event_lambda',
    version='1.0',
    description='Exmaple of lambda listening to cloudwatch events and then posting to sns with a specific subject',
    author='Galen Dunkleberger',
    license='ASL',
    zip_safe=False,
    include_package_data=True,
    package_dir={"": "source"},
    packages=find_packages("source"),
    test_suite='tests'
)
