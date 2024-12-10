# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/10

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 10

    # @answer(1234)
    def part_1(self) -> int:
        row = len(self.input)
        col = len(self.input[0])
        for i in range(row):
            self.input[i] = list(self.input[i])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = []
        ans = 0
        
        for i in range(row):
            for j in range(col):
                char = self.input[i][j]
                if char == '0':
                    nine_set = set()
                    stack.append((char, i, j))
                    while len(stack) != 0:
                        value, x, y = stack.pop()
                        for dx, dy in directions:
                            if x + dx >= 0 and x + dx < row and y + dy >= 0 and y + dy < col and self.input[x + dx][y + dy].isnumeric():
                                if int(self.input[x + dx][y + dy]) == int(value) + 1:
                                    stack.append((self.input[x + dx][y + dy], x + dx, y + dy))
                        if int(value) == 9:
                            nine_set.add((value, x, y))
                    ans += len(nine_set)
                    
        return ans
    # @answer(1234)
    def part_2(self) -> int:
        row = len(self.input)
        col = len(self.input[0])
        for i in range(row):
            self.input[i] = list(self.input[i])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        stack = []
        ans = 0
        
        for i in range(row):
            for j in range(col):
                char = self.input[i][j]
                if char == '0':
                    stack.append((char, i, j))
                    while len(stack) != 0:
                        value, x, y = stack.pop()
                        for dx, dy in directions:
                            if x + dx >= 0 and x + dx < row and y + dy >= 0 and y + dy < col and self.input[x + dx][y + dy].isnumeric():
                                if int(self.input[x + dx][y + dy]) == int(value) + 1:
                                    stack.append((self.input[x + dx][y + dy], x + dx, y + dy))
                        if int(value) == 9:
                            ans += 1
                    
        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
