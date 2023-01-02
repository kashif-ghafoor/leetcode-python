import string


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hashMap = {}
        code = 97
        for char in key:
            if (char == ' ' or hashMap.get(char)):
                continue
            hashMap[char] = chr(code)
            code += 1
        output = ''
        for letter in message:
            if (letter == ' '):
                output += ' '
                continue
            output += hashMap[letter]
        return output
