from distutils.core import setup
from setuptools import find_packages

setup(
    name='ibeaconscanner',
    version='0.0.1',
    url='https://github.com/konradko/iBeacon-scanner',
    packages=find_packages(),
    long_description=open('README.md').read(),
    install_requires=[
        'PyBluez==0.22',
    ],
)
