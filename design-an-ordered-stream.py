from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = ['']*n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        key = idKey - 1
        self.stream[key] = value
        if (key == self.pointer):
            result = [value]
            flag = True
            while (flag and self.pointer < self.n - 1):
                if (self.stream[self.pointer+1] == ''):
                    flag = False
                else:
                    result.append(self.stream[self.pointer+1])
                self.pointer += 1
            return result
        else:
            return []
