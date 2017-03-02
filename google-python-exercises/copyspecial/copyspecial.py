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

"""Copy Special exercise
"""

def docommand(cmd):
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write('doing', cmd, 'there was an error:', output)
    sys.exit(1)
  return output

def getPaths(dir):
  path = os.path.abspath(dir)
  if os.path.exists(path):
    cmd = 'ls -l '+path
    output = docommand(cmd)
    selectedOutput = re.findall('[\w.]*__[\w.]+__[\w.]+', output)
    result = [] 
    for eachfile in selectedOutput:
      result.append(os.path.join(path, eachfile))
      # print '...' , os.path.join(path, eachfile) 
    return result

def copytodir(todir, files):
  todir = os.path.abspath(todir)
  print 'coptodir ', todir
  if not os.path.exists(todir):
    cmd = 'mkdir '+ todir
    # print 'about to do ', cmd
    # return
    output = docommand(cmd) 
  else:
    print todir, 'exists'
  
  # now copy them
  for sourcepath in files:
    filename = os.path.basename(sourcepath)
    destpath = os.path.join(todir, filename)
    # print 'about to do shutil.copy from', sourcepath, ' to ', destpath
    # return
    shutil.copy(sourcepath, destpath)
  return

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

  # +++your code here+++
  files = getPaths(args[0])
  if todir:
    copytodir(todir, files)
    return
  if tozip:
    ziptodir(tozip, files)
    print 'tozip'
    return
  else:
    for eachfile in files:
      print eachfile
  
if __name__ == "__main__":
  main()
