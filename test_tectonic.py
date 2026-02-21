import random

def tectonic_shuffle(arr):
    n = len(arr)
    if n < 3:
        return arr
        
    iterations = 3
    for _ in range(iterations):
        # 1. Pick a fault line
        fault = random.randint(1, n - 2)
        
        # 2. Shockwave
        arr[:fault] = reversed(arr[:fault])
        arr[fault:] = reversed(arr[fault:])
        
        # 3. Subduction (Array shift)
        subduction_point = random.randint(1, n - 1)
        arr[:] = arr[subduction_point:] + arr[:subduction_point]
        
    return arr



test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]


print( "techtonic shuffle test" )
print( test_array )
result = tectonic_shuffle(test_array)
print( result )
