Title: 01. Two Sum
Date: 2016-09-06 11:36
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-01-Two_Sum
Authors: Weezer Su
Summary: First question on leetcode

starting working on leetcode now.

    :::python
    class Solution:
    # @return a tuple, (index1, index2)
      def twoSum(self, num, target):
          d = {}
          for pos, i in enumerate(num):
              if d.has_key(target - i):
                  return [d[target - i], pos]
              d[i] = pos 
	    
    
