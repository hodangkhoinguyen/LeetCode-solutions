"""
    Problem: https://leetcode.com/problems/group-anagrams/description
    Approach: hashing the frequency of characters to a string or a tuple (in Python)
    Time Complexity: O(nk), n is the length of the list and k is the length of a string
    Space Complexity: O(nk)
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def parse_word(word):
            """
            Convert a word to a tuple of letter frequency

            Args:
                word: str
            """
            freq = [0] * 26
            for i in word:
                freq[ord(i) - ord('a')] += 1
            return tuple(freq)

        # A dictionary with key as the parsing value and value as a list of anagrams
        groups = dict()
        for word in strs:
            parse_value = parse_word(word)
            groups.setdefault(parse_value, [])
            groups[parse_value].append(word)
        return groups.values()
