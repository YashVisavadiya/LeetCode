from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        n = len(nums)

        # Find the maximum OR value from the array
        for num in nums:
            max_or |= num

        count = 0
        # Iterate through all possible subsets using bit manipulation
        for mask in range(1 << n):
            current_or = 0
            for i in range(n):
                if mask & (1 << i):
                    current_or |= nums[i]
            if current_or == max_or:
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.countMaxOrSubsets([3, 1]))  # Output: 2
    print(sol.countMaxOrSubsets([2, 2, 2]))  # Output: 7
    print(sol.countMaxOrSubsets([3, 2, 1, 5]))  # Output: 6
