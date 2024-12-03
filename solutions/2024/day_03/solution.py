# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import TextSolution, answer
import re

class Solution(TextSolution):
    _year = 2024
    _day = 3

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        matchlist = re.findall(pattern="mul\(\d*\,\d*\)", string=self.input)
        for match in matchlist:
            splitlist = match.split(",")
            leftnumber = int(splitlist[0][4:])
            rightnumber = int(splitlist[1][:-1])
            ans += (leftnumber * rightnumber)
        
        return ans        
    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        matchlist = re.findall(pattern="mul\(\d*\,\d*\)|don\'t\(\)|do\(\)", string=self.input)
        print(matchlist)
        flag = 1
        for match in matchlist:
            if match == "don't()":
                flag = 0
            elif match == "do()":
                flag = 1
            else:
                if flag == 0:
                    continue
                else:
                    splitlist = match.split(",")
                    leftnumber = int(splitlist[0][4:])
                    rightnumber = int(splitlist[1][:-1])
                    ans += (leftnumber * rightnumber)
        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
