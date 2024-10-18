from typing import List
from itertools import combinations


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        answer = Answer()
        max_or = self.max_or_from_array(nums)

        for i in range(1, len(nums) + 1):
            for combination in combinations(nums, i):
                if self.max_or_from_array(combination) == max_or:
                    answer.count += 1

        return answer.count

    @staticmethod
    def max_or_from_array(nums):
        max_or = 0

        for num in nums:
            max_or |= num

        return max_or


class Answer:
    def __init__(self):
        self.count = 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.countMaxOrSubsets([3, 1]))  # Output: 2
    print(sol.countMaxOrSubsets([2, 2, 2]))  # Output: 7
    print(sol.countMaxOrSubsets([3, 2, 1, 5]))  # Output: 6
