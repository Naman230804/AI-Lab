def find_min_max(arr):
    if not arr:
        return None, None  # handle empty list
    minimum = maximum = arr[0]
    for num in arr[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return minimum, maximum

# Example usage
numbers = [23, 1, 56, -4, 88, 12, 0]
min_val, max_val = find_min_max(numbers)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")