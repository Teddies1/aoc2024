# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer
from ...utils.example import checksafe

class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    # @answer(1234)
    def part_1(self) -> int:
        numsafe = 0
        for i in self.input:
            arr = (list(map(int, i.split())))
            if checksafe(arr):
                numsafe += 1
                
        return numsafe 

    # @answer(1234)
    def part_2(self) -> int:
        numsafe = 0
        for numbers in self.input:
            arr = (list(map(int, numbers.split())))
            if checksafe(arr):
                numsafe += 1
            else:
                flag = 0
                for i in range(len(arr) + 1):
                    nums = arr[:i] + arr[i + 1 :]
                    if checksafe(nums):
                        flag = 1
                if flag == 1:    
                    numsafe += 1
                flag = 0 
                
        return numsafe

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
