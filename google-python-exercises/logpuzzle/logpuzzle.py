#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  try:
    f = open(filename, 'rU')
  except IOError:
    print 'problem trying to open ', filename
    sys.exit(1)

  lines = f.readlines()
  wanted_urls = []
  dict = {}
  for line in lines:
    m = re.search(r'google-python-class/images/puzzle/([\w-]+.jpg)',line) 
    # trying this for second puzzle:
    # m = re.search(r'google-python-class/images/puzzle/[\w-]+(\w\w\w\w.jpg)',line)
    if m:
      # add to dictionary with key of jpg and value of URL
      if m.group(1) not in dict:
        dict[m.group(1)] = \
          'http://code.google.com/edu/languages/google-python-class/images/puzzle/' +m.group(1) 
  # print dict
  for jpg in sorted(dict.keys()):
    wanted_urls.append(dict[jpg])
  return wanted_urls

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  dest_dir = os.path.abspath(dest_dir)
  print'here1'
  if not os.path.exists(dest_dir):
    try:
      # print 'about to do mkdir ', dest_dir
      # return
      os.mkdir(dest_dir)
    except IOError:
      print 'trouble with mkdir: ', dest_dir
      sys.exit(1)
  i = 0
  for url in img_urls:
    destpath = os.path.join(dest_dir, 'img'+str(i)+'.jpg')
    print 'fetching: ', url
    urllib.urlretrieve(url, destpath)
    i += 1

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
