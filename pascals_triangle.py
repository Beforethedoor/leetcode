from math import factorial
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            rez = []
            for j in range(i+1):
                rez.append(factorial(i)//(factorial(j)*factorial(i-j)))
            result.append(rez)
        return result


obj = Solution()
print(obj.generate(numRows=5))
