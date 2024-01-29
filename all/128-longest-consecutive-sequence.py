"""
    Problem: https://leetcode.com/problems/longest-consecutive-sequence/
    Approach:
        Use a set to keep track of numbers
        Iterate through the set and find the lowest number of a sequence - the number that doesn't have the next lower number in the set 
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Add numbers to set
        distinct = set()
        for i in nums:
            distinct.add(i)

        result = 0
        # Iterate through numbers in set
        for i in distinct:
            # Check if that's the lowest number of a sequence
            if i - 1 in distinct:
                continue

            # Find the length of the sequence
            curr = i
            while curr + 1 in distinct:
                curr += 1
            length = curr - i + 1
            if length > result:
                result = length
        return result
