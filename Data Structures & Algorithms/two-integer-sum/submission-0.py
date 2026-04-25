from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # dictionary to store number -> index

        for i in range(len(nums)):
            complement = target - nums[i]

            # Check if complement exists in dictionary
            if complement in seen:
                return sorted([seen[complement], i])

            # Store current number and its index
            seen[nums[i]] = i
        
        