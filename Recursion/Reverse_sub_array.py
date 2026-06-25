
###  Reverse a part of the array
##  [2,3,4,5,6,4,3,2,4] l = 3, r = 5   --->> [2,3,6,5,4,4,3,2,4]



#using Recursion

class Solution:
    def reverse_sub_arr(self,arr,l,r):
        if l > r:
            return arr
        
        arr[l-1],arr[r-1] = arr[r-1],arr[l-1]

        return self.reverse_sub_arr(arr,l+1,r-1)

s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7]
result = s.reverse_sub_arr(arr,2,4)
print(result)
print(arr)  # call by reference

#output:
# [1, 4, 3, 2, 5, 6, 7]
# [1, 4, 3, 2, 5, 6, 7]


