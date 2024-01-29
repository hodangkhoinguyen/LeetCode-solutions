"""
    Problem: https://leetcode.com/problems/top-k-frequent-elements/
    Approach:
        Count the frequency of each distinct numbers
        Use an array whose indices as the frequency. Each element is a list of the numbers with the same frequency
    Time Complexity: O(n)
    Space Complexity: O(n) for frequency and arr
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Count the occurences of distinct numbers
        freq = dict()
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        # Based on the frequency, use a list whose indinces are the number of occurences
        # Then the corresponding element is a list of all numbers with the same frequency
        arr = [[] for x in range(len(nums) + 1)]
        for num, f in freq.items():
            arr[f].append(num)

        # Go top-down to add the numbers to the result until reach k elements
        result = []
        for i in range(len(nums), 0, -1):
            for num in arr[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
