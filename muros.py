import unittest


class Solution:
    @staticmethod
    def canReachN(a, k, m):
        dp = [-float("inf") for _ in range(len(a))]
        dp[0] = m
        for i in range(len(dp)):
            for j in range(k + 1):
                x = i - j
                if x >= 0:
                    dif = a[i]-a[x] if a[i]-a[x] >= 0 else 0
                    dp[i] = max(dp[i], dp[x] - dif)
        return dp[-1] >= 0


class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertTrue(Solution.canReachN([1, 2, 2, 1, 3, 2, 1], 2, 4))

    def test_two(self):
        self.assertFalse(Solution.canReachN([1, 2, 2, 1, 3, 2, 1], 2, 1))


if __name__ == '__main__':
    unittest.main()
