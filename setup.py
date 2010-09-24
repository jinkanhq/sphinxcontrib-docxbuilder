# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os, sys

version = '0.0.1'
long_description = \
        open(os.path.join("src","README.txt")).read() + \
        open(os.path.join("src","TODO.txt")).read()

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    #"Development Status :: 3 - Alpha",
    #"Development Status :: 4 - Beta",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Topic :: Office/Business :: Office Suites",
    "Topic :: Software Development :: Documentation",
    "Topic :: Text Processing :: Markup",
]

setup(
     name='sphinxcontrib-docxbuilder',
     version=version,
     description='Sphinx docx builder extension.',
     long_description=long_description,
     classifiers=classifiers,
     keywords=['sphinx','extension','builder', 'docx','OpenXML'],
     author='Takayuki SHIMIZUKAWA',
     author_email='shimizukawa at gmail dot com',
     url='http://bitbucket.org/shimizukawa/sphinxcontrib-docxbuilder',
     license='MIT',
     packages=find_packages('src'),
     package_dir={'': 'src'},
     package_data = {'': ['buildout.cfg']},
     include_package_data=True,
     install_requires=[
        'Sphinx',
        'docx',  # docx included this package
        # -*- Extra requirements: -*-
        'lxml',  # required by docx
        'PIL',  # required by docx
     ],
     extras_require=dict(
         test=[
             'Nose',
             'minimock',
             'pep8',
         ],
     ),
     test_suite='nose.collector',
     tests_require=['Nose','minimock','pep8'],
     zip_safe=False,
)

