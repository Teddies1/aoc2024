# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/7

from ...base import StrSplitSolution, answer
import itertools

class Solution(StrSplitSolution):
    _year = 2024
    _day = 7

    # @answer(1234)
    def part_1(self) -> int:
        ans = set()
        for inp in self.input:
            inp = inp.split(":")
            value = int(inp[0])
            operands = inp[1].split(" ")[1:]
            operator_length = len(operands) - 1            
            operators = ["+", "*"]
            
            for ops in itertools.product(operators, repeat=operator_length):
                operand_pointer = 0
                stack = operands[::-1]
                while len(stack) != 1:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    intermediate = 0
                    if ops[operand_pointer] == "*":
                        intermediate += num1 * num2
                        stack.append(intermediate)
                        operand_pointer += 1
                    else:
                        intermediate += num1 + num2
                        stack.append(intermediate)
                        operand_pointer += 1
                if stack[0] == value:
                    ans.add(stack[0])   
                
        return sum(ans)
            
            

    # @answer(1234)
    def part_2(self) -> int:
        ans = set()
        for inp in self.input:
            inp = inp.split(":")
            value = int(inp[0])
            operands = inp[1].split(" ")[1:]
            operator_length = len(operands) - 1            
            operators = ["+", "*", "||"]
            
            for ops in itertools.product(operators, repeat=operator_length):
                operand_pointer = 0
                stack = operands[::-1]
                while len(stack) != 1:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    intermediate = 0
                    if ops[operand_pointer] == "*":
                        intermediate += num1 * num2
                        stack.append(intermediate)
                        operand_pointer += 1
                    elif ops[operand_pointer] == "||":
                        intermediate = str(num1) + str(num2)
                        stack.append(int(intermediate))
                        operand_pointer += 1
                    else:
                        intermediate += num1 + num2
                        stack.append(intermediate)
                        operand_pointer += 1
                if stack[0] == value:
                    ans.add(stack[0])   
                
        return sum(ans)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
