"""
    Problem: https://leetcode.com/problems/valid-anagram/
    Approach: hash map
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        def char_map(word):
            """
            Convert characters in word to a frequency map with key as character and value as occurrences

            Args:
                word: str
            """
            freq = dict()
            for ch in s:
                freq.setdefault(ch, 0)
                freq[ch] += 1
            return freq

        map_s = char_map(s)
        map_t = char_map(t)
        for ch in map_s:
            if map_s[ch] != map_t.get(ch):
                return False
        return True
