# coding: utf-8
import os
from setuptools import setup

README = os.path.join(os.path.dirname(__file__), 'README.md')


setup(
    name='python_boilerplate',
    version='0.1',
    description='This is a simple Python project skeleton.',    
    author="your name",
    author_email="youremail@mail.com",
    license= "MIT",    
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_user/name_project',    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
