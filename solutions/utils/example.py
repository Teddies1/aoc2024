# add whatever utilities you'll find useful across multiple solutions
# import them in a solution using:
# from ...utils.example import add


def add(a: int, b: int):
    return a + b

def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))

def strictly_decreasing(L):
    return all(x>y for x, y in zip(L, L[1:]))

def strictly_monotonic(L):
    return strictly_increasing(L) or strictly_decreasing(L)

def check_difference(L):
    n = len(L)
    for i in range(0, n-1):
        if abs(L[i] - L[i+1]) > 3 or abs(L[i] - L[i+1]) < 1:
            return False
        
    return True

def checksafe(arr: list[int]):
    if strictly_monotonic(arr):
        return check_difference(arr)
    
    return False

def return_coordinates(matrix):    
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "^":
                return i, j

def move_char(direction, x, y):
    if direction == "up":
        return go_up(x, y)
    if direction == "down":
        return go_down(x, y)
    if direction == "left":
        return go_left(x, y)
    if direction == "right":
        return go_right(x, y)
        
def go_up(x, y):
    return x-1, y

def go_right(x, y):
    return x, y+1

def go_left(x, y):
    return x, y-1

def go_down(x, y):
    return x+1, y

def obstacle_infront(direction, matrix, x, y):
    if direction == "up":
        if x-1 >= 0:
            if matrix[x-1][y] == "#":
                return "obstacle"
        else:
            return "exit"
        
    if direction == "down":
        if x+1 < len(matrix):
            if matrix[x+1][y] == "#":
                return "obstacle"
        else:
            return "exit"
        
    if direction == "right":
        if y+1 < len(matrix[0]):
            if matrix[x][y+1] == "#":
                return "obstacle"
        else:
            return "exit"
        
    if direction == "left":
        if y-1 >= 0:
            if matrix[x][y-1] == "#":
                return "obstacle"
        else:
            return "exit"
        
    return "proceed"
    
def change_dir(direction):
    if direction == "up":
        return "right"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"
    if direction == "right":
        return "down"