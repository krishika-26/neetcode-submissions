class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for i in nums:
            diff = i - 1

            if diff in nums_set:
                continue

            current_num = i
            current_len = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_len += 1

            longest = max(longest, current_len)

        return longest
        