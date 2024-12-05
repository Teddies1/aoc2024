# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    # @answer(1234)
    def part_1(self) -> int:
        n = len(self.input)
        m = len(self.input[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if self.input[i][j] != 'X':
                    continue
                if j < m-3 and self.input[i][j] == 'X' and self.input[i][j+1] == 'M' and self.input[i][j+2] == 'A' and self.input[i][j+3] == 'S':
                    ans += 1          
                if j >= 3 and self.input[i][j] == 'X' and self.input[i][j-1] == 'M' and self.input[i][j-2] == 'A' and self.input[i][j-3] == 'S':
                    ans += 1
                if i < n-3 and self.input[i][j] == 'X' and self.input[i+1][j] == 'M' and self.input[i+2][j] == 'A' and self.input[i+3][j] == 'S':
                    ans += 1
                if i >= 3 and self.input[i][j] == 'X' and self.input[i-1][j] == 'M' and self.input[i-2][j] == 'A' and self.input[i-3][j] == 'S':
                    ans += 1
                if i < n-3 and j < m-3 and self.input[i][j] == 'X' and self.input[i+1][j+1] == 'M' and self.input[i+2][j+2] == 'A' and self.input[i+3][j+3] == 'S':
                    ans += 1
                if j >= 3 and i >= 3 and self.input[i][j] == 'X' and self.input[i-1][j-1] == 'M' and self.input[i-2][j-2] == 'A' and self.input[i-3][j-3] == 'S':
                    ans += 1
                if i >= 3 and j < m-3 and self.input[i][j] == 'X' and self.input[i-1][j+1] == 'M' and self.input[i-2][j+2] == 'A' and self.input[i-3][j+3] == 'S':
                    ans += 1  
                if j >= 3 and i < n-3 and self.input[i][j] == 'X' and self.input[i+1][j-1] == 'M' and self.input[i+2][j-2] == 'A' and self.input[i+3][j-3] == 'S':
                    ans += 1          
        return ans
    # @answer(1234)
    def part_2(self) -> int:
        n = len(self.input)
        m = len(self.input[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                '''
                M.S
                .A.
                M.S
                
                S.M
                .A.
                S.M
                
                M.M
                .A.
                S.S
                
                S.S
                .A.
                M.M
                '''
                if self.input[i][j] != 'A':
                    continue
                if i >= 1 and j >= 1 and i < n-1 and j < m-1 and self.input[i][j] == 'A' and self.input[i+1][j+1] == 'M' and self.input[i-1][j-1] == 'S' and self.input[i+1][j-1] == 'S' and self.input[i-1][j+1] == 'M':
                    ans += 1
                if i >= 1 and j >= 1 and i < n-1 and j < m-1 and self.input[i][j] == 'A' and self.input[i+1][j+1] == 'S' and self.input[i-1][j-1] == 'M' and self.input[i+1][j-1] == 'M' and self.input[i-1][j+1] == 'S':
                    ans += 1 
                if i >= 1 and j >= 1 and i < n-1 and j < m-1 and self.input[i][j] == 'A' and self.input[i+1][j+1] == 'M' and self.input[i-1][j-1] == 'S' and self.input[i+1][j-1] == 'M' and self.input[i-1][j+1] == 'S':
                    ans += 1
                if i >= 1 and j >= 1 and i < n-1 and j < m-1 and self.input[i][j] == 'A' and self.input[i+1][j+1] == 'S' and self.input[i-1][j-1] == 'M' and self.input[i+1][j-1] == 'S' and self.input[i-1][j+1] == 'M':
                    ans += 1
                        
        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
