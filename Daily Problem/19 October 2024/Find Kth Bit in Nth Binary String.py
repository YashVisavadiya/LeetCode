class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev = curr = '0'

        for i in range(2, n + 1):
            curr = prev + '1' + self.reversed_invert(prev)
            prev = curr

        return curr[k - 1]

    def reversed_invert(self, s: str) -> str:
        return ''.join(['1' if c == '0' else '0' for c in s])[::-1]


if __name__ == "__main__":
    sol = Solution()

    print(sol.findKthBit(3, 1))  # 0
    print(sol.findKthBit(4, 11))  # 1
    print(sol.findKthBit(1, 1))  # 0
    print(sol.findKthBit(2, 3))  # 1
