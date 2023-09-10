#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# chdmanbatch.py by shinrax2
VERSION = "0.2"

#built-in
import subprocess
import shlex
import sys
import shutil
import platform
import os


def call(cmd):
    if platform.system() != "Windows":
        cmd = shlex.split(cmd)
    return subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0].decode("utf8")

def getfiles(dirpath, filetypes = [".cue", ".iso"]):
    f =  []
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            if os.path.isfile(os.path.join(root, file)):
                f.append(os.path.join(root, file))
    newfiles = []
    for file in f:
        for filetype in filetypes:
            if file.endswith(filetype) == True:
                newfiles.append(file)
    return newfiles

def getbasedir():
    if getattr(sys, "frozen", False):
        basedir = sys.executable
    else:
        basedir = __file__
    return os.path.dirname(basedir)

print(f"chdmanbatch verison {VERSION} by shinrax2")

searchpath = [getbasedir(), os.getcwd()]
chdman = "chdman"
if platform.system() == "Windows":
    chdman = f"{chdman}.exe"

if (shutil.which(chdman) is not None) == False:
    print(f"this tool requires \"{chdman}\" to be on PATH!")
    sys.exit(0)

chdman_exe = os.path.abspath(shutil.which(chdman))
force = False
deleteinput = False

if "-f" in sys.argv:
    force = True
    sys.argv.remove("-f")

if "--deleteinput" in sys.argv:
    deleteinput = True
    sys.argv.remove("--deleteinput")

if len(sys.argv[1:]) > 0:
    searchpath = sys.argv[1:]
paths = ""
for dir in searchpath:
    paths = f"{paths} {os.path.abspath(dir)}"
print(f"chdman executable: {chdman_exe}")
print(f"search path(s):{paths}")
print(f"overwrite files: {'yes' if force == True else 'no'}")
print(f"delete input files: {'yes' if deleteinput == True else 'no'}")

i = 1
l = len(searchpath)
for dir in searchpath:
    files = getfiles(dir)
    l2 = len(files)
    i2 = 1
    print(f"searching dir {i} of {l}: {os.path.abspath(dir)}")
    print(f"found {l2} supported files")
    for file in files:
        print(f"compressing file {i2} of {l2}")
        inputfile = os.path.abspath(file)
        outputfile = f"{os.path.splitext(os.path.abspath(file))[0]}.chd"
        cmd = f"{chdman_exe} createcd --input \"{inputfile}\" --output \"{outputfile}\" --numprocessors {os.cpu_count()}"
        print(f"input file: {inputfile}")
        print(f"output file: {outputfile}")
        if os.path.exists(outputfile) == True:
            print("output file already exists")
            if force == True:
                print("overwriting output file")
                cmd = f"{cmd} --force"
        if os.path.exists(outputfile) == False or force == True:
            print(f"chdman commandline: {cmd}")
            print(call(cmd))
        else:
            print("skipping file")
        if deleteinput == True:
            print(f"deleting input file\"{inputfile}\"")
            os.remove(inputfile)
        i2 += 1
    i += 1
