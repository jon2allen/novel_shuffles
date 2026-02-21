
 

import random

def pendulum_shuffle(arr):
    left, right = 0, len(arr) - 1
    turn = 0
    
    while left < right:
        j = random.randint(left, right)
        if turn % 2 == 0:
            arr[left], arr[j] = arr[j], arr[left]
            left += 1
        else:
            arr[right], arr[j] = arr[j], arr[right]
            right -= 1
        turn += 1
    return arr


arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

shuf1 = pendulum_shuffle(arr)

print("shuf1: ", shuf1 )
