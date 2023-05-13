from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # [["A","B","C","E"],
        #  ["S","F","C","S"],
        #  ["A","D","E","E"]]
        # "ABCCED"

        rows = len(board)
        columns = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= columns
                    or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))
            res = (
                dfs(r-1, c, i+1) or
                dfs(r, c-1, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r+1, c, i+1)
            )
            path.remove((r, c))
            return res

        for row in range(rows):
            for col in range(columns):
                if dfs(row, col, 0):
                    return True

        return False


obj = Solution()
print(obj.exist(
    board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    word="ABCCED"
    )
)
