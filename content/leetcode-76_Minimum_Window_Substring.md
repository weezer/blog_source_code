Title:76. Minimum Window Substring 
Date: 2016-11-30 11:29
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-76_Minimum_Window_Substring 
Authors: Weezer Su
Summary: Minimum Window Substring
抄的，以后再说吧。

```python
class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        if (target == ""):
            return ""
        S , T = source, target
        d, dt = {}, dict.fromkeys(T, 0)
        for c in T: d[c] = d.get(c, 0) + 1
        pi, pj, cont = 0, 0, 0
        if (source =="" or target ==""):
            return ""
        ans = ""
        while pj < len(S):
            if S[pj] in dt:
                if dt[S[pj]] < d[S[pj]]:
                    cont += 1
                dt[S[pj]] += 1;
            if cont == len(T):
                while pi < pj:
                    if S[pi] in dt:
                        if dt[S[pi]] == d[S[pi]]:
                            break;
                        dt[S[pi]] -= 1;
                    pi+= 1
                if ans == '' or pj - pi < len(ans):
                    ans = S[pi:pj+1]
                dt[S[pi]] -= 1
                pi += 1
                cont -= 1
            pj += 1
        return ans
```

rough solution, if you want to u can use a count to count the number to reduce the branches.
```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        min_window = None
        first_point = 0
        second_point = 0
        string_length = len(s)
        dup_string = list(t)
        while first_point < string_length:
            if s[first_point] in dup_string:
                dup_string.remove(s[first_point])
            if len(dup_string) == 0:
                if min_window is None:
                    min_window = s[:first_point+1]
                while True:
                    if s[second_point] in t:
                        if len(min_window) > first_point - second_point:
                            min_window = s[second_point:first_point+1]
                        first_point = second_point
                        second_point += 1
                        dup_string = list(t)
                        break
                    second_point += 1
            first_point += 1
        return min_window
```
这个没有考虑连续字符情况。
```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        p_head, p_tail = 0, 0
        t_dict = dict.fromkeys(t, 0)
        flag_set = set(t)
        ans = ""
        while p_head < len(s):
            if s[p_head] in t:
                t_dict[s[p_head]] += 1
                if s[p_head] in flag_set:
                    flag_set.remove(s[p_head])
            if len(flag_set) == 0:
                while p_tail < p_head:
                    if s[p_tail] in t:
                        if t_dict[s[p_tail]] == 1:
                            break
                        t_dict[s[p_tail]] -= 1
                    p_tail += 1
                if len(ans) == 0 or p_head - p_tail < len(ans):
                    ans = s[p_tail: p_head+1]
                t_dict[s[p_tail]] -= 1
                flag_set.add(s[p_tail])
                p_tail += 1
            p_head += 1
        return ans
```
