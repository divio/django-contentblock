'''
setup.py version 0.0.1
current version: https://gist.github.com/8668de36c00ca78df172
This is a standard re-usable setup.py file for django apps.
This file should stay untouched. Instead create a file called metadata.py.

metadata.py example:

package_name = 'gsa'
name = 'django-gsa'
author = 'Divio GmbH'
author_email = 'developers@divio.ch'
description = "A thin wrapper for using a Google Search Appliance (GSA) for searches in django.s."
version = '0.1.0'
project_url = 'http://github.com/divio/%s' % name
license = 'BSD'

If you have data files you want to include, please create a MANIFEST.in file.
setup.py is called with include_package_data=True, so packade data will be
automatically read and included based on MANIFEST.in (or from svn if you 
happen to use it)
'''

# do not change anything in here
# edit metadata.py and MANIFEST.in instead
import metadata as m

from setuptools import setup, find_packages

install_requires = [
    'setuptools',
]

setup(
    name = m.name,
    version = m.version,
    url = m.project_url,
    license = m.license,
    platforms=['OS Independent'],
    description = m.description,
    author = m.author,
    author_email = m.author_email,
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data = True, #Accept all data files and directories matched by MANIFEST.in or found in source control.
    package_dir = {
        m.package_name:m.package_name,
    },
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)