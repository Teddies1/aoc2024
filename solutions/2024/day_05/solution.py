# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 5

    # @answer(1234)
    def part_1(self) -> int:
        for i, string in enumerate(self.input):
            if string == '':
                ordering_list = self.input[:i]
                page_numbers = self.input[i+1:]
                
        ans = 0
        valid_pages = []
        precedence_dict = {}
        for order in ordering_list:
            number_list = order.split("|")
            first_number = number_list[0]
            second_number = number_list[1]
            if first_number not in precedence_dict:
                precedence_dict[first_number] = [second_number]
            else:
                precedence_dict[first_number].append(second_number)
                
        for page_number in page_numbers:
            flag = 0
            page_list = page_number.split(",")
            n = len(page_list)
            for i in range(n):
                for j in range(i+1, n):
                    if page_list[i] not in precedence_dict or page_list[j] not in precedence_dict[page_list[i]]:
                        flag = 1
            if flag == 0:
                valid_pages.append(page_list)
            flag = 0
            
        
        for valid_page in valid_pages:
            n = len(valid_page)
            mid = n // 2 
            ans += int(valid_page[mid])     
                
        return ans
                
    # @answer(1234)
    def part_2(self) -> int:
        for i, string in enumerate(self.input):
            if string == '':
                ordering_list = self.input[:i]
                page_numbers = self.input[i+1:]
                
        ans = 0
        invalid_pages = []
        precedence_dict = {}
        for order in ordering_list:
            number_list = order.split("|")
            first_number = number_list[0]
            second_number = number_list[1]
            if first_number not in precedence_dict:
                precedence_dict[first_number] = [second_number]
            else:
                precedence_dict[first_number].append(second_number)
                
        for page_number in page_numbers:
            flag = 0
            page_list = page_number.split(",")
            n = len(page_list)
            for i in range(n):
                for j in range(i+1, n):
                    if page_list[i] not in precedence_dict or page_list[j] not in precedence_dict[page_list[i]]:
                        flag = 1
            if flag == 1:
                invalid_pages.append(page_list)
            flag = 0
            
        for invalid_page in invalid_pages:
            indegree_dict = {}
            n = len(invalid_page)
            for i in range(n):
                indegree_dict[invalid_page[i]] = 0
                for j in range(n):
                    if invalid_page[i] in precedence_dict and invalid_page[j] in precedence_dict[invalid_page[i]]:
                        indegree_dict[invalid_page[i]] += 1
                        
            sorted_indegree = list(dict(sorted(indegree_dict.items(), key=lambda item: item[1], reverse=True)).keys())
            n = len(sorted_indegree)
            mid = n // 2 
            ans += int(sorted_indegree[mid])
            indegree_dict = {}

        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
