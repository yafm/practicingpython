#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
#  print 'nums=', nums, '--------------------'
  adjRemoved = []
  for index in range(len(nums) - 1):
#    print 'index=', index, 'nums[index]=', nums[index]
    if nums[index] != nums[index+1]:
      adjRemoved.append(nums[index])
#      print 'adjRemoved=',adjRemoved
  if len(nums) > 1: 
    adjRemoved.append(nums[-1])
  return adjRemoved


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  print  'list1 and list2 =', list1, list2
  # if either lists are empty, take care of that
  if len(list1) == 0: 
    return list2
  if len(list2) == 0: 
    return list1

  # here both lists have entries
  merged = []
  l1 = 0
  l2 = 0
  while l1 < len(list1) or l2 < len(list2): 
#   print 'i1, ij, merged ',l1, l2, merged
    if list1[l1] < list2[l2]:
      merged.append(list1[l1])
      l1+=1
      # have we reached the end of one list?
      if l1 == len(list1):
        merged.extend(list2[l2:])
#       print '&&& i1, ij, merged ',l1, l2, merged
        return merged
    else:
      merged.append(list2[l2])
      l2+=1
      if l2 == len(list2):
        merged.extend(list1[l1:])
#       print '&&& i1, ij, merged ',l1, l2, merged
        return merged
  return merged

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])
  test(linear_merge([], ['aa', 'bb', 'bb']),
       ['aa', 'bb', 'bb'])
  test(linear_merge(['aa', 'aa'],[] ),
       ['aa', 'aa'])
  test(linear_merge([],[] ),
       [])
  test(linear_merge(['aa', 'aa','ww','y'], ['aa', 'bb', 'bb','bc']),
       ['aa', 'aa', 'aa', 'bb', 'bb','bc','ww','y'])


if __name__ == '__main__':
  main()
