# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/14

from ...base import StrSplitSolution, answer
import re
import time
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import matplotlib.pyplot as plt


class Solution(StrSplitSolution):
    _year = 2024
    _day = 14

    # @answer(1234)
    def part_1(self) -> int:
        row = 103
        col = 101
        map = {}
        for inp in self.input:
            px, py, vx, vy = [int(d) for d in re.findall(r'-?\d+', inp)]
            for _ in range(100):
                px += vx
                if px < 0:
                    px += col
                elif px >= col:
                    px -= col
                # 2 4 4 1 6 -2 > 6 5
                py += vy
                if py < 0:
                    py += row
                elif py >= row:
                    py -= row
                
            if (px, py) in map:
                map[(px, py)] += 1
            else:
                map[(px, py)] = 1
        
        grid = [["."] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if (j, i) in map:
                    grid[i][j] = map[(j, i)]
        
        quadrant_row = (row - 1) // 2
        quadrant_col = (col - 1) // 2
        # 0,0, 6,0 0,4 6,4
        q1, q2, q3, q4 = 0, 0, 0, 0
        for i in range(quadrant_row):
            for j in range(quadrant_col):
                if grid[i][j] != ".":
                    q1 += int(grid[i][j])
                if grid[i + quadrant_row + 1][j] != ".":
                    q2 += int(grid[i + quadrant_row + 1][j])
                if grid[i][j + quadrant_col + 1] != ".":
                    q3 += int(grid[i][j + quadrant_col + 1])
                if grid[i + quadrant_row + 1][j + quadrant_col + 1] != ".":
                    q4 += int(grid[i + quadrant_row + 1][j + quadrant_col + 1])
                    
        return q1 * q2 * q3 * q4
        

        

    # @answer(1234)
    def part_2(self) -> int:
        row = 103
        col = 101
        # row = 7
        # col = 11
        map = {}
        positions = []
        velocities = []
        
        for inp in self.input:
            px, py, vx, vy = [int(d) for d in re.findall(r'-?\d+', inp)]
            positions.append((px, py))
            velocities.append((vx, vy))
            
        robots = len(positions)
        
        for i in range(robots):
            px, py = positions[i]
            vx, vy = velocities[i]
            
            if (px, py) in map:
                map[(px, py)] += 1
            else:
                map[(px, py)] = 1
                    
        iterations = 0
        while(True):
            print(iterations)
            for i in range(robots):
                px, py = positions[i]
                vx, vy = velocities[i]
                
                map[(px, py)] -= 1
                if map[(px, py)] == 0:
                    del map[(px, py)]
                    
                px += vx
                if px < 0:
                    px += col
                elif px >= col:
                    px -= col
                # 2 4 4 1 6 -2 > 6 5
                py += vy
                if py < 0:
                    py += row
                elif py >= row:
                    py -= row
                    
                if (px, py) in map:
                    map[(px, py)] += 1
                else:
                    map[(px, py)] = 1
                    
                positions[i] = (px, py)
            
                grid = [[0] * col for _ in range(row)]
                for i in range(row):
                    for j in range(col):
                        if (j, i) in map:
                            grid[i][j] = map[(j, i)]
                    # print(grid[i])
                        
            # print(grid)
            iterations += 1
            plt.imsave(f'output/name{iterations}.png', grid)
            # time.sleep(0.5)
            

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
