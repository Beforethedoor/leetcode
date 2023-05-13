from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat

        flat = []
        for i in mat:
            flat.extend(i)

        output = []
        for i in range(r):
            output.append(flat[i*c:(i+1)*c])
        return output


obj = Solution()
print(obj.matrixReshape(mat=[[1, 2], [3, 4], [5, 6], [7, 8]], r=2, c=4))
