from setuptools import setup, find_packages
from pathlib import Path


setup(
    name='data',
    version='0.0.1',
    description='OpenKE dataset as python package',
    packages=['benchmarks'],
    install_requires=install_requires,
    zip_safe=False)
