import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='drf-json-keyformat',
    version='0.1.0',
    packages=['drf_json_keyformat'],
    include_package_data=True,
    license='BSD License',
    description='Use camelCase and different JSON key formats with Django REST Framework.',
    long_description=README,
    url='https://github.com/krisjacyna/drf-json-keyformat',
    author='Kris Jacyna',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
