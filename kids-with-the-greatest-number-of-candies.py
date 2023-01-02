class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        maxCandies = max(candies)
        for candy in candies:
            if candy+extraCandies >= maxCandies:
                results.append(True)
            else:
                results.append(False)
        return results
