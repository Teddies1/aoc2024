# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/9

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 9

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0 
        n, pointer = len(self.input), 0
        file_string = []
        for i in range(n):
            if i % 2 == 0:
                for _ in range(int(self.input[i])):
                    file_string.append(str(pointer))
                pointer += 1
            else:
                for _ in range(int(self.input[i])):
                    file_string.append(".")
                    
        m = len(file_string)
        left, right = 0, m-1
        while left < right:
            if file_string[left] == "." and file_string[right].isnumeric():
                file_string[left], file_string[right] = file_string[right], file_string[left]
                left += 1
                right -= 1
            elif file_string[left].isnumeric():
                left += 1
            elif file_string[right] == ".":
                right -= 1
                
        for i in range(m):
            if file_string[i].isnumeric():
                ans += (int(i) * int(file_string[i]))
                
        return ans
    # @answer(1234)
    def part_2(self) -> int:
        ans = 0 
        n, pointer = len(self.input), 0
        file_string = []
        freq_map = {}
        blank_map = {}
        
        for i in range(n):
            if i % 2 == 0:
                freq_map[pointer] = (len(file_string), int(self.input[i]))
                for _ in range(int(self.input[i])):
                    file_string.append(str(pointer))
                pointer += 1
            else:
                blank_map[len(file_string)] = int(self.input[i])
                for _ in range(int(self.input[i])):
                    file_string.append(".")
        
        freq_map = dict(reversed(freq_map.items()))        
        m = len(file_string)
        
        for k, v in freq_map.items():
            for start_pos, length in blank_map.items():
                if v[1] <= length and start_pos < v[0]:
                    i, j = v[0], start_pos
                    for _ in range(v[1]):
                        file_string[i], file_string[j] = file_string[j], file_string[i]
                        i += 1
                        j += 1
                    break
            blank_map = {}
            ptr = 0
            while ptr < len(file_string):
                if file_string[ptr] == '.':
                    i = ptr
                    blank_map[i] = 0
                    while ptr < len(file_string) and file_string[ptr] == '.':
                        blank_map[i] += 1
                        ptr += 1
                else:
                    ptr += 1    
            
        for i in range(m):
            if file_string[i].isnumeric():
                ans += (int(i) * int(file_string[i]))
                
        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
