#!/usr/bin/env python

class Solution(object):
        def longest_substring(self,s):
                substring = []
                rv  = 0
                for c in s:
                        if c not in substring:
                                substring.append(c)
                        else:
                                substring = substring[substring.index(c) + 1:]
                                substring.append(c)
                        if len(substring) > rv:
                                rv = len(substring)
                return rv

a = Solution()

s = 'bb'

print(a.longest_substring(s))
