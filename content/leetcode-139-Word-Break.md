Title:139. Word Break 
Date: 2017-02-21 17:07
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-139-Word-Break 
Authors: Weezer Su
Summary: Word Break 

DFS

```python
ass Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not len(s) or not len(wordDict):
            return False
        if len(s) == 1:
            if s in wordDict:
                return True
            else:
                return False
        word_array = (len(s) + 1) * [False]
        word_array[0] = True
        max_len_word = max(map(len, wordDict)) + 1
        for i in range(len(word_array)):
            if word_array[i] is False:
                continue
            else:
                for j in range(1, min(max_len_word, len(s) - i + 1)):
                    print s[i:i+j]
                    if s[i:i+j] in wordDict:
                        word_array[i+j] = True
        print word_array
        return word_array[len(s)]

```

