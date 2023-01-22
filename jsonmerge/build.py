#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import PyInstaller.__main__

args = [
    "--name=jsonmerge",
    "--clean",
    "--onefile",
    "jsonmerge.py"
]
PyInstaller.__main__.run(args)
