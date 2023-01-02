class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i, val in enumerate(encoded):
            result.append(result[i] ^ val)
        return result
