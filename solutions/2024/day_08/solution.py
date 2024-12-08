# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/8

from ...base import StrSplitSolution, answer
from ...utils.example import check_valid

class Solution(StrSplitSolution):
    _year = 2024
    _day = 8

    # @answer(1234)
    def part_1(self) -> int:
        character_locations = {}
        row = len(self.input)
        col = len(self.input[0])
        
        for i in range(row):
            self.input[i] = list(self.input[i])
        for i in range(row):
            for j in range(col):
                char = self.input[i][j]
                if char != ".":
                    if char not in character_locations:
                        character_locations[self.input[i][j]] = []
                        character_locations[self.input[i][j]].append((i, j))
                    else:
                        character_locations[self.input[i][j]].append((i, j))
                        
        ans = 0
        ans_set = set()
        for k, v in character_locations.items():
            for i in range(len(v)):
                for j in range(len(v)):
                    if j == i:
                        continue
                    else:
                        x1, y1 = v[i]
                        x2, y2 = v[j]
                        newx = x2 + (x2 - x1)
                        newy = y2 + (y2 - y1)
                        if check_valid(newx, newy, row, col):
                            ans_set.add((newx, newy))
                   
        return len(ans_set)
    # @answer(1234)
    def part_2(self) -> int:
        
        character_locations = {}
        row = len(self.input)
        col = len(self.input[0])
        ans_set = set()
        
        for i in range(row):
            self.input[i] = list(self.input[i])
        for i in range(row):
            for j in range(col):
                char = self.input[i][j]
                if char != ".":
                    ans_set.add((i, j))
                    if char not in character_locations:
                        character_locations[self.input[i][j]] = []
                        character_locations[self.input[i][j]].append((i, j))
                    else:
                        character_locations[self.input[i][j]].append((i, j))
                        
        ans = 0
        for k, v in character_locations.items():
            for i in range(len(v)):
                for j in range(len(v)):
                    if j == i:
                        continue
                    else:
                        x1, y1 = v[i]
                        x2, y2 = v[j]
                        newx = x2 + (x2 - x1)
                        newy = y2 + (y2 - y1)
                        while check_valid(newx, newy, row, col):
                            ans_set.add((newx, newy))
                            newx += (x2 - x1)
                            newy += (y2 - y1)
                   
        return len(ans_set)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
