import random

def fisher_yates_shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

def adaptive_block_shuffle(arr, block_size):
    n = len(arr)
    k = n // block_size
    blocks = [arr[i*block_size : (i+1)*block_size] for i in range(k)]

    for block in blocks:
        fisher_yates_shuffle(block)

    fisher_yates_shuffle(blocks)

    shuffled = []
    for block in blocks:
        shuffled.extend(block)

    return shuffled

# Example usage:
arr = list(range(20))
shuffled = adaptive_block_shuffle(arr, block_size=5)
print(shuffled)
