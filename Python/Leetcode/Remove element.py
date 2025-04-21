#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
#The remaining elements of nums are not important as well as the size of nums.

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

def removeElement(Nums, Val):
    k = 0
    for i in range (len(Nums)):
         if Nums[i] != Val:
            Nums[k] = Nums[i]
            k += 1
    return k
        

print(removeElement(nums, val))
print (nums)


