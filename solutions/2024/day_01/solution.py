# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, IntSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(1651298)
    def part_1(self) -> int:
        list1, list2 = [], []
        ans = 0
        for inp in self.input:
            inplist = inp.split(" ")
            list1.append(int(inplist[0]))
            list2.append(int(inplist[-1]))

        list1.sort()
        list2.sort()
        
        n = len(list1)
        
        for i in range(n):
            ans += abs(list1[i] - list2[i])
            
        return ans
    @answer(21306195)
    def part_2(self) -> int:
        list1, map = [], {}
        
        ans = 0
        for inp in self.input:
            inplist = inp.split(" ")
            list1.append(int(inplist[0]))
            if int(inplist[-1]) in map:
                map[int(inplist[-1])] += 1
            else: 
                map[int(inplist[-1])] = 1
        
        for i in list1:
            if i in map:
                ans += (i * map[i])
            
        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

#source .venv/bin/activate