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

