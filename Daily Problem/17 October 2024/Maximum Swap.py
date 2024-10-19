class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        max_num = sorted(num_str, reverse=True)
        n = len(num_str)

        for i in range(n):
            if num_str[i] != max_num[i]:
                for j in range(n - 1, i, -1):
                    if num_str[j] == max_num[i]:
                        num_str[i], num_str[j] = num_str[j], num_str[i]
                        return int("".join(num_str))
        return num


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumSwap(2736))  # Output: 7236
    print(sol.maximumSwap(9973))  # Output: 9973
    print(sol.maximumSwap(98368))  # Output: 98863