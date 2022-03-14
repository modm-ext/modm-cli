#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019, Niklas Hauser
#
# This file is part of the modm project.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup

setup(
    name = "modm",
    version = "0.1.2",
    python_requires=">=3.5.0",

    install_requires = ["lbuild", "lxml", "pyelftools"],

    # Metadata
    author = "Niklas Hauser",
    author_email = "niklas@salkinium.com",
    description = "modm command-line interface",
    long_description="Currently only used for grouping dependencies.",
    license = "MPLv2",
    url = "https://modm.io",
    classifiers = [
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: Embedded Systems",
    ],
)
