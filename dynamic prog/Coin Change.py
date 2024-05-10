# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.
from typing import List,Optional,Union,Dict,Tuple



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.dfs(coins, amount, 0, {})
        return int(result) if result != float('inf') else -1

    def dfs(self, coins: List[int], amount: int, i: int, cache: Dict[Tuple[int, int], Union[int,float]]) -> Union[int, float]:
        if (amount, i) in cache:
            return cache[(amount, i)]

        if amount < 0:
            return float('inf')  # Impossible combination, return infinity
        if amount == 0:
            return 0

        if i == len(coins):
            return float('inf')  # No more coins available, return infinity

        # Explore all possible choices (take or skip the current coin)
        take_coin = self.dfs(coins, amount - coins[i], i, cache)
        take_coin += 1  # Increment count for taking current coin
        cache[(amount - coins[i], i)] = take_coin

        skip_coin = self.dfs(coins, amount, i + 1, cache)
        cache[(amount, i + 1)] = skip_coin

        return min(take_coin, skip_coin)








sol = Solution()
coins = [1,2,5]
amount = 11

print(sol.coinChange(coins,amount)) #3


coins = [2]
amount = 3
print(sol.coinChange(coins,amount)) #-1
