#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dirs):
    """ get files with special names in dirs """
    abs_paths = []
    for d in dirs:
        fnames = os.listdir(d)
        for f in fnames:
            match = re.search(r'.*__\w+__.*', f)
            if match:
                abs_paths.append( os.path.abspath(f))
        
    return abs_paths


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  abs_paths = get_special_paths(args)
  
  if todir:
      if not os.path.exists(todir):
        os.makedirs(todir)
        
      for f in abs_paths:
          shutil.copy(f,todir)
          
  if tozip:
      cmd = 'zip -j ' + tozip + ' ' + ' '.join(abs_paths)
      print "cmd: " + cmd
      
      (status, output) = commands.getstatusoutput(cmd)
      # If command had a problem (status is non-zero),
      # print its output to stderr and exit.
      if status:
          sys.stderr.write(output)
          sys.exit(1)
      
      """try:
          subprocess.check_call(cmd)
      except subprocess.CalledProcessError as e:
          print e.output"""
      
  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
