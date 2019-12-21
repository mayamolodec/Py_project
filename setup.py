from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Phoenix_interpol',
    version='1.0',
    include_package_data=True,
    packages=find_packages(),
    test_suite='test',
    install_requires=['numpy>=1.13', 'scipy>=1.0', 'astropy>=3.2.1'],
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
) 
