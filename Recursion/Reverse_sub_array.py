
###  Reverse a part of the array
##  [2,3,4,5,6,4,3,2,4] l = 3, r = 5   --->> [2,3,6,5,4,4,3,2,4]



#using Recursion


class Solution:
    # method 1
    def reverse_sub_arr(self,arr,l,r):
        if l > r:
            return arr
        
        arr[l-1],arr[r-1] = arr[r-1],arr[l-1]

        return self.reverse_sub_arr(arr,l+1,r-1)  # passes arr all the way up ✅
    
    #mehtod 2
    def reverse_sub_arr2(self,arr,l,r):
        if l> r:
            return arr
        arr[l-1],arr[r-1] = arr[r-1], arr[l-1]

        self.reverse_sub_arr2(arr,l+1,r-1) # ← return value is DROPPED (return dropped, doesn't matter)

        return arr  # first caller always gets arr ✅
    
    # wrong method(critical mistake)
    def reverse_sub_arr3(self,arr,l,r):
        if l> r:
            return arr    
        
        arr[l-1],arr[r-1] = arr[r-1], arr[l-1]

        self.reverse_sub_arr3(arr,l+1,r-1)  # result is IGNORED
        # implicitly returns None


s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7]
result = s.reverse_sub_arr(arr,2,4)
print(result)  # [1, 4, 3, 2, 5, 6, 7]
print(arr)  # [1, 4, 3, 2, 5, 6, 7]          # call by reference (arr itself IS modified)


arr = [1, 2, 3, 4, 5, 6, 7]
result2 = s.reverse_sub_arr2(arr,2,4)
print(result2)  # [1, 4, 3, 2, 5, 6, 7]
print(arr)  # [1, 4, 3, 2, 5, 6, 7]          # call by reference (arr itself IS modified)



arr = [1, 2, 3, 4, 5, 6, 7]
result3 = s.reverse_sub_arr3(arr,2,4)
print(result3)  # None
print(arr)   # [1, 4, 3, 2, 5, 6, 7]         # call by reference (arr itself IS modified)





