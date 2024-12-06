# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import StrSplitSolution, answer
from ...utils.example import return_coordinates, change_dir, obstacle_infront, move_char
import copy
import time

class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    # @answer(1234)
    def part_1(self) -> int:
        for i in range(row):
            self.input[i] = list(self.input[i])
            
        row = len(self.input)
        col = len(self.input[0])
        matrix = copy.deepcopy(self.input)
        current_dir = "up"
        x, y = return_coordinates(matrix)
        matrix[x][y] = "X"
        ans = 0
        
        while obstacle_infront(current_dir, matrix, x, y) != "exit":
            x, y = move_char(current_dir, x, y)
            matrix[x][y] = "X"
            status = obstacle_infront(current_dir, matrix, x, y)
            if status == "obstacle":
                current_dir = change_dir(current_dir)
                
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "X":
                    ans += 1
        
        return matrix
    
    # @answer(1234)
    def part_2(self) -> int:
        updated_matrix = self.part_1()
        matrix = copy.deepcopy(self.input)
        ways = 0
        row = len(self.input)
        col = len(self.input[0])
        
        for i in range(row):
            for j in range(col):
                if updated_matrix[i][j] == "X":
                    if matrix[i][j] != "^":
                        matrix[i][j] = "#"
                        current_dir = "up"
                        x, y = return_coordinates(matrix)
                        visited = set()
                        visited.add((x, y, current_dir))
                        while obstacle_infront(current_dir, matrix, x, y) != "exit":
                            x, y = move_char(current_dir, x, y)
                            if (x, y, current_dir) in visited:
                                ways += 1
                                break
                            else:
                                visited.add((x, y, current_dir))
                            status = obstacle_infront(current_dir, matrix, x, y)
                            while status == "obstacle":
                                current_dir = change_dir(current_dir)
                                status = obstacle_infront(current_dir, matrix, x, y)
                        matrix[i][j] = "."
                    else:
                        current_dir = "up"
                        x, y = return_coordinates(matrix)
                        visited = set()
                        visited.add((x, y, current_dir))
                        while obstacle_infront(current_dir, matrix, x, y) != "exit":
                            x, y = move_char(current_dir, x, y)
                            if (x, y, current_dir) in visited:
                                ways += 1
                                break
                            else:
                                visited.add((x, y, current_dir))
                            status = obstacle_infront(current_dir, matrix, x, y)
                            while status == "obstacle":
                                current_dir = change_dir(current_dir)
                                status = obstacle_infront(current_dir, matrix, x, y)
                        matrix[i][j] = "^"
                        
        return ways

                        
    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
