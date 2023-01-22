## chdmanbatch

this tool recursively searches trought given directories for ".cue" files and converts them to compressed ".chd" files with `chdman` for use with emulators like [Duckstation](https://github.com/stenzek/duckstation).

## requirements

* Python 3
* `chdman` in your PATH variable or next to this script

## usage

you can either

1. copy this script into the directory where your ".cue" files are stored and run it. by default it will recursively search for them in the directory its located.

2. supply the directory as commandline argument like this:

      `python3 chdmanbatch.py /home/user/cuefiles` **or** `python3 chdmanbatch.py "c:\\cuefiles"`

".chd" file will be stored next to the converted ".cue" file.

## flags

1. `-f`: the force flag forces the script to overwrite the output file if it already exists. default: off
