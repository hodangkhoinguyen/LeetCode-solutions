"""
    Problem: https://leetcode.com/problems/contains-duplicate/description
    Approach: hash set
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

def containsDuplicate(self, nums) -> bool:
    # Set to keep track of what numbers are iterated
    seen_numbers = set()
    for num in nums:
        # If number is in the set, this is a duplicate
        if num in seen_numbers:
            return True
        seen_numbers.add(num)

    return False
