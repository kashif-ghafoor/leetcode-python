class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(list(map(lambda account: sum(account), accounts)))
