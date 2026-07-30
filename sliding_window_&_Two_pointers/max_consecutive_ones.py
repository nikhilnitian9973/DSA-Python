
# Brute Force solution
# T.C. = O(n*(n+1)/2) =  O(n^2)
# S.C. = O(1)

def max_consecutive_ones(nums,k):
    maxi = 0
    for i in range(len(nums)):
        zeros = 0
        for j in range(i,len(nums)):
            if nums[j] == 0:
                zeros +=1
            if zeros > k:
                break
            maxi = max(maxi,j-i+1)
    return maxi
nums = [1,1,0,0,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1]
k = 2
print(max_consecutive_ones(nums,k))


# Better solution
# T.C. = O(n) + O(n) = O(2n) = O(n)
# S.C. = O(1)

def max_consecutive_ones1(nums,k):
    left = 0
    right = 0
    maxi = 0
    zeros = 0
    while right < len(nums):
        if nums[right] == 0:
            zeros +=1
        while zeros > k:
            if nums[left] == 0:
                zeros -=1
            left +=1
        maxi = max(maxi,right - left +1)
        right +=1
    return maxi

print(max_consecutive_ones1(nums,k))
        
#Optimal solution
#T.C = O(n)
#S.C = O(1)

def max_consecutive_ones2(nums,k):
    left = 0
    right = 0
    maxi = 0
    zeros = 0
    while right < len(nums):
        if nums[right] == 0:
            zeros +=1
        if zeros > k:
            if nums[left] == 0:
                zeros -=1
            left +=1
        maxi = max(maxi,right - left +1)
        right +=1
    return maxi

print(max_consecutive_ones2(nums,k))