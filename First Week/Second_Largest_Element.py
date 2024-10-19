def find_second_largest(array):
    if len(array) < 2:
        return "-1"
    
    # Descending order
    sorted_array = sorted(array, reverse=True)
    
    # Second largest element
    return sorted_array[1]

# Array
numbers = [10, 24, 56, 75, 99]

# Call function
second_largest = find_second_largest(numbers)

# Print
print("The second largest element in the array is:", second_largest)
