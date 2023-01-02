class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            exists = False
            pointer = -1
            if (haystack[i] == needle[0]):
                pointer = i
                for j in range(0, len(needle)):
                    if (len(haystack) > i+j and needle[j] == haystack[i+j]):
                        if (j+1 == len(needle)):  # last item of needle
                            exists = True
                    else:
                        break
            if (exists):
                return pointer
        return -1
