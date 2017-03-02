#!/usr/bin/python -tt
# jag's practising around

import sys

def Hello(name):
  if name == 'Alice' or name == '1':
    print 'Alice mode'
    name = name + '??'
  else:
    name = name + '!!'
  print "Hello", name 

def main():
  print sys.argv
  Hello(sys.argv[1])


# boilerplate code
if __name__ == '__main__':
  main()

