# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/12

from ...base import StrSplitSolution, answer
from collections import defaultdict, Counter, deque 

class Solution(StrSplitSolution):
    _year = 2024
    _day = 12

    # @answer(1234)
    def part_1(self) -> int:
        row = len(self.input)
        col = len(self.input[0])
        
        for i in range(row):
            self.input[0] = list(self.input[0])
            
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        visited = set()
        for i in range(row):
            for j in range(col):
                if (self.input[i][j], i, j) in visited:
                    continue
                area = 0
                total_peri = 0
                char = self.input[i][j]
                stack = deque([(char, i, j)])
                while len(stack) != 0:
                    value, x, y = stack.popleft()
                    visited.add((value, x, y))
                    peri = 4
                    area += 1
                    for dx, dy in directions:
                        if x + dx >= 0 and x + dx < row and y + dy >= 0 and y + dy < col and self.input[x + dx][y + dy] == value: 
                            peri -= 1
                            if (self.input[x + dx][y + dy], x + dx, y + dy) not in visited and (self.input[x + dx][y + dy], x + dx, y + dy) not in stack:
                                stack.append((self.input[x + dx][y + dy], x + dx, y + dy))
                    total_peri += peri
                ans += (total_peri * area)
        return ans
                

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
