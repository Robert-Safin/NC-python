from typing import List, Dict, Tuple

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.dfs(amount, coins, 0, {})

    def dfs(self, amount: int, coins: List[int], i: int, cache: Dict[Tuple[int, int], int]) -> int:
        # Check if the result for the current amount and index is already in the cache
        if (amount, i) in cache:
            return cache[(amount, i)]

        # Base cases
        if i == len(coins):
            return 0
        if amount < 0:
            return 0
        if amount == 0:
            return 1

        # Calculate the number of ways using the current coin and without using it
        ways_with_current_coin = self.dfs(amount - coins[i], coins, i, cache)
        ways_without_current_coin = self.dfs(amount, coins, i + 1, cache)

        # Update the cache with the sum of both ways
        cache[(amount, i)] = ways_with_current_coin + ways_without_current_coin

        return cache[(amount, i)]



sol = Solution()
amount = 5
coins = [1,2,5]
print(sol.change(amount,coins)) # Output: 4
