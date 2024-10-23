nums = [1, 1, 1]        #Output = 2 (1, 1 - 1, 1)
A = 2
OtherNums = [1, 2, 3]   #Output = 2 (1, 2 - 3)
B = 3

def subarraySum(nums, k):
    # Initialize a dictionary to store cumulative sum counts
    sum_map = {0: 1}
    current_sum = 0
    count = 0
    
    # Traverse through the array
    for num in nums:
        current_sum += num
        
        # Check if current_sum - k exists in sum_map
        if current_sum - k in sum_map:
            count += sum_map[current_sum - k]
        
        # Update the sum_map with current_sum
        sum_map[current_sum] = sum_map.get(current_sum, 0) + 1
    
    return count

print(subarraySum(nums, A))
print(subarraySum(OtherNums, B))
