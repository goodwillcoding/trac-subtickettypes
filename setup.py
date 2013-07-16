#!/usr/bin/env python

 #
 # Copyright 2009, Michael R <none@example.com>
 # All rights reserved. Distributed under the terms of the MIT License.
 #

from setuptools import setup

def main():
    setup(
        name='TracSubTicketTypes',
        version='0.1',
        packages=['subtickettypes'],
        package_data={ 'subtickettypes': ['htdocs/*.js'] },

        author='Michael R',
        author_email='none@example.com',
        description='Provides support for sub ticket types in the Trac interface.',
        license='BSD',
        keywords='trac plugin ticket types subtickettypes',
        url='',
        classifiers=[
            'Framework :: Trac',
            'Development Status :: 1 - Planning',
            # 'Development Status :: 2 - Pre-Alpha',
            # 'Development Status :: 3 - Alpha',
            # 'Development Status :: 4 - Beta',
            # 'Development Status :: 5 - Production/Stable',
            # 'Development Status :: 6 - Mature',
            # 'Development Status :: 7 - Inactive',
            'Environment :: Web Environment',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
        ],

        install_requires=['Trac>=1.0dev',],

        entry_points={
            'trac.plugins': [
                'subtickettypes.web_ui=subtickettypes.web_ui',
            ]
        }
    )

if __name__ == "__main__":
    main()