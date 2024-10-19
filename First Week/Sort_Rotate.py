def check_sorted_and_rotated(arr):
    n = len(arr)
    
    break_count = 0
    
    for i in range(n):
        
        if arr[i] > arr[(i + 1) % n]:
            break_count += 1
    
    return break_count == 1

# Arrays
arr1 = [3, 4, 5, 1, 2]

# Print
print(check_sorted_and_rotated(arr1))
