#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# sfind.py by shinrax2

import os
import sys

def getfiles(dirpath):
    f =  []
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            if os.path.isfile(os.path.join(root, file)):
                f.append(os.path.join(root, file))
    f.sort(key=str.lower)
    return f

try:
    search = str(sys.argv[1])
    dir = sys.argv[2]
except IndexError:
    print('find "string to search" "folder to search"')

for file in getfiles(dir):
    with open(file, "rb") as f:
        try:
            if search in f.read().decode("utf-8"):
                print(file)
        except UnicodeDecodeError:
            pass