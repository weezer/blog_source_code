Title: 03. Longest Substring Without Repeating Characters
Date: 2016-09-14 21:16
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-3-Longest_Substring_Without_Repeating_Characters
Authors: Weezer Su
Summary: 3rd question on leetcode

    :::python
    class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            maxl = 0
            length = 0
            ls = []
            for i in s:
                if i not in ls:
                    ls.append(i)
                    length += 1
                else:
                    ls = ls[ls.index(i)+1:]
                    ls.append(i)
                    length = len(ls)
                if length > maxl:
                        maxl = length
            return maxl
