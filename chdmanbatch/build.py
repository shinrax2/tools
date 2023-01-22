#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import PyInstaller.__main__

args = [
    "--name=chdmanbatch",
    "--clean",
    "--onefile",
    "chdmanbatch.py"
]
PyInstaller.__main__.run(args)
