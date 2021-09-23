# -*- coding: utf-8 -*-

"""
Copyright (c) 2021 Keitaro AB
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = '1.0.0'

setup(
    name='ckanext-issues',
    version=version,

    # description
    description='CKAN Extension providing Issues (Task/Todos/...)',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/keitaroinc/ckanext-issues',

    # Author details
    author='''Keitaro Inc''',
    author_email='''info@keitaro.com''',

    # License
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    # What does your project relate to?
    keywords='''CKAN ckanext issues''',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext', 'ckanext.issues'],

    include_package_data=True,
    package_data={},

    zip_safe=False,
    install_requires=[
        'enum34',
    ],
    entry_points="""
    [ckan.plugins]
    issues=ckanext.issues.plugin:IssuesPlugin

    [babel.extractors]
    ckan = ckan.lib.extract:extract_ckan
    """,

    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
