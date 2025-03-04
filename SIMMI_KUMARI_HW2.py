import time

def num_paths(m, n):

    if m == 1 or n == 1:
        return 1
    # Recursive case: sum the paths by moving down and moving right
    return num_paths(m - 1, n) + num_paths(m, n - 1)

def num_paths_memo(m, n):
    memo = {}

    # Check if the result is already computed
    if (m, n) in memo:
        return memo[(m, n)]

    # Base case: If we reach the first row or first column, there's only one path
    if m == 1 or n == 1:
        return 1
    
    # Recursive case: sum the paths by moving down and moving right
    result = num_paths_memo(m - 1, n) + num_paths_memo(m, n - 1)

    # Store the computed result in the global memo dictionary
    memo[(m, n)] = result
    return result
    

#driver code - you do not need to make any changes after this line.
#However, submit a screenshot of the output to report the execution time/elapsed time.
start_time = time.time()
print(num_paths(15,14))
end_time = time.time()

start_time_memo = time.time()
print(num_paths_memo(15,14))
end_time_memo = time.time()

print(f"Elapsed time (no memoization): {end_time - start_time} seconds")
print(f"Elapsed time (memoization): {end_time_memo - start_time_memo} seconds")
