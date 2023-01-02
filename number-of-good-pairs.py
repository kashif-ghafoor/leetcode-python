from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = 0

        for i, num in enumerate(nums):
            for j in range(i, len(nums)):
                if (nums[i] == nums[j] and i != j):
                    goodPairs += 1

        return goodPairs


nums = [1, 2, 3, 1, 1, 3]

sol = Solution().numIdenticalPairs(nums)
print(sol)

# O(n^2) Time Complexity
# O(n) Time complexity
# O(1) auxiliary space
