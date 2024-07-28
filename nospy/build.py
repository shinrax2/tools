#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import PyInstaller.__main__

args = [
    "--name=nos_autoclose",
    "--clean",
    "--onefile",
    "--windowed",
    "autoclose.py"
]
PyInstaller.__main__.run(args)
