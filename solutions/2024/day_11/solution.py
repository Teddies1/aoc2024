# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/11

from ...base import StrSplitSolution, answer
from ...utils.example import process_stones

class Solution(StrSplitSolution):
    _year = 2024
    _day = 11

    # @answer(1234)
    def part_1(self) -> int:
        stone_string = self.input[0].split()
        for i in range(25):
            stone_string = process_stones(stone_string)
        return len(stone_string)

    # @answer(1234)
    def part_2(self) -> int:
        stone_string = self.input[0].split()
        dict = {}
        for stone in stone_string:
            if stone in dict:
                dict[stone] += 1
            else:
                dict[stone] = 1
        for i in range(75):
            new_dict = {}
            for k in dict.copy():
                v = dict[k]
                dict[k] -= v
                if dict[k] == 0:
                    del dict[k]
                if int(k) == 0:
                    if '1' in new_dict:
                        new_dict['1'] += v
                    else:
                        new_dict['1'] = v
                elif len(str(k)) % 2 == 0:
                    mid = (len(str(k)) // 2) 
                    left_half, right_half = str(int((k)[:mid])), str(int((k)[mid:]))
                    if left_half in new_dict:
                        new_dict[left_half] += v
                    else:
                        new_dict[left_half] = v
                    if right_half in new_dict:
                        new_dict[right_half] += v
                    else:
                        new_dict[right_half] = v
                else:
                    if str(int(k) * 2024) in new_dict:
                        new_dict[str(int(k) * 2024)] += v
                    else:
                        new_dict[str(int(k) * 2024)] = v
            dict = new_dict
            
        ans = 0
        for k, v in dict.items():
            ans += v
        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
