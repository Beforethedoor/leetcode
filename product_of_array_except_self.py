from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1 for i in range(n)]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        postfix = [1 for i in range(n)]
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        res = []
        for i in range(n):
            res.append(prefix[i]*postfix[i])

        return res


obj = Solution()
print(obj.productExceptSelf(nums=[1, 2, 3, 4]))
