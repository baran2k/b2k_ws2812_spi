#!/usr/bin/env python

from distutils.core import setup

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware',
               'Topic :: System :: Hardware :: Hardware Drivers']

setup(	name		= "b2k_ws2812_spi",
	version		= "0.1",
	description	= "Python bindings for WS2812 communication over SPI.MOSI",
	long_description= open('README.md').read() + "\n" + open('CHANGELOG.md').read(),
	author		= "baran2k",
	author_email	= "baran2k@mail.ru",
	maintainer	= "baran2k",
	maintainer_email= "baran2k@mail.ru",
	license		= "GPLv2",
	classifiers	= classifiers,
	url		= "none",
        py_modules      = ['b2k_ws2812_spi'],
)
