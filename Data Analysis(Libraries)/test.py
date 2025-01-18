def count_pairs(arr):
    remainder_counts = [0, 0]  # Counts of remainders 0 and 1
    for num in arr:
        remainder_counts[num % 2] += 1
    
    # Calculate count of pairs
    count = (remainder_counts[0] * (remainder_counts[0] - 1) // 2)  # Pairs with remainder 0
    # count += (remainder_counts[1] * (remainder_counts[1] - 1) // 2) // 2  # Pairs with remainder 1

    return count 

# Example usage
arr = [1, 2, 3, 4, 5]
print(count_pairs(arr))  # Output will depend on the array elements

