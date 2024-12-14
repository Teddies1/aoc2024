# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/13

from ...base import StrSplitSolution, answer
import re

class Solution(StrSplitSolution):
    _year = 2024
    _day = 13

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        buttonA: str = []
        buttonB: str = []
        prizes: str = []
        for case in self.input:
            if "Button A" in case:
                buttonA.append(case)
            if "Button B" in case:
                buttonB.append(case)
            if "Prize" in case:
                prizes.append(case)
                
        n = len(buttonA)
        
        for i in range(n):
            x1, y1 = [int(s) for s in re.findall(r'\b\d+\b', buttonA[i])]
            x2, y2 = [int(s) for s in re.findall(r'\b\d+\b', buttonB[i])]
            x3, y3 = [int(s) for s in re.findall(r'\b\d+\b', prizes[i])]
            for x in range(100):
                for y in range(100):
                    x_value = (x * x1) + (y * x2)
                    y_value = (x * y1) + (y * y2)
                    if x_value == x3 and y_value == y3:
                        print(x, y)
                        ans += (3 * x) + y
                        
        return ans
    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        buttonA: str = []
        buttonB: str = []
        prizes: str = []
        for case in self.input:
            if "Button A" in case:
                buttonA.append(case)
            if "Button B" in case:
                buttonB.append(case)
            if "Prize" in case:
                prizes.append(case)
                
        n = len(buttonA)
        
        for i in range(n):
            x1, y1 = [int(s) for s in re.findall(r'\b\d+\b', buttonA[i])]
            x2, y2 = [int(s) for s in re.findall(r'\b\d+\b', buttonB[i])]
            x3, y3 = [int(s) + 10000000000000 for s in re.findall(r'\b\d+\b', prizes[i])]
            
            y = round(((x3 * y1) - (y3 * x1)) / ((x2 * y1) - (y2 * x1)))
            x = round(((x3 * y2) - (y3 * x2)) / ((y2 * x1) - (x2 * y1)))
            
            if (x * x1) + (y * x2) == x3 and (x * y1) + (y * y2) == y3:
                print(x, y)
                ans += (3 * int(x)) + int(y)
            
        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
