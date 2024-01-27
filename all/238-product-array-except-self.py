"""
    Problem: https://leetcode.com/problems/product-of-array-except-self
    Approach:
        The first loop calculates the product from left to right
        The second loop calculates the product from right to left
    Time Complexity: O(n)
    Space Complexity: O(1) excluding the result array
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        curr = 1

        # Calculate the product of previous numbers of a certain position, called A
        for i in range(len(nums)):
            ans.append(curr)
            curr *= nums[i]

        curr = 1
        # Calculate the product of succeeding numbers of a certain position, then multiply it by A
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= curr
            curr *= nums[i]

        return ans
