from setuptools import setup, find_packages
from os.path import join, dirname

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='Phoenix_interpol',
    version='0.0.1',
    include_package_data=True,
    packages=find_packages(),
    scripts=['Phoenix_interpol.py'],
    test_suite='test',
    entry_points={'console_scripts':['ph_interp = Phoenix_interpol:with_args']},
    install_requires=['numpy>=1.13', 'scipy>=1.0', 'astropy>=3.0.1'],
    long_description=long_description,
) 
