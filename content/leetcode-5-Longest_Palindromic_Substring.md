Title: 05. Longest Palindromic Substring
Date: 2016-09-15 00:30
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-5-Longest_Palindromic_Substring
Authors: Weezer Su
Summary: First time use dynamic programing to resolve leetcode question

dynamic programming, but defintely is not the answer they want, i gonna check the internet.

    :::python
    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """
            if len(s) <= 1:
                return s
            d_max = {}
            dp_matrix = [[0 for x in range(len(s))] for y in range(len(s))]
            for i in range(len(s)):
                dp_matrix[i][i] = 1
            d_max[1] = 1
            for j in range(1, len(s)):
                for i in range(j)[::-1]:
                    if (s[i] == s[j] and dp_matrix[i+1][j-1]) is not False:
                        dp_matrix[i][j] = dp_matrix[i+1][j-1] +2
                        if d_max.get(dp_matrix[i][j]) is None:
                            d_max[dp_matrix[i][j]] = i
                    else:
                        dp_matrix[i][j] = False
    
            start_pos = d_max[max(d_max.keys())]
            return s[start_pos:start_pos+max(d_max.keys())]
