#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse


# This is to help coaches and graders identify student assignments
__author__ = "dbmiddle"

special_files = []


def get_special_paths(dir):
    file_names = os.listdir(dir)
    for file_name in file_names:
        matches = re.search(r'__\w+__', file_name)
        if matches:
            if matches.group() in file_name:
                special_files.append(os.path.abspath(file_name))
    for special_file in special_files:
        print(special_file)


def copy_to(paths, dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)
    for path in paths:
        destination = os.path.join(dir, os.path.basename(path))
        shutil.copy(path, destination)


def zip_to(paths, zippath):
    command = ['zip', '-j', zippath]
    command.extend(paths)
    subprocess.check_output(command)


def main():
    get_special_paths(os.getcwd())
    # copy_to(special_files[0], os.getcwd())
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='destination directory')
    args = parser.parse_args()

    todir = args.todir
    tozip = args.tozip

    if todir:
        copy_to(special_files, todir)
    elif tozip:
        zip_to(special_files, tozip)
    else:
        print(special_files)

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong
    # (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
