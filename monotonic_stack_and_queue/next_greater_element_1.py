#Brute Force solution 1
# T.C = O(n*(n+1)/2) = O(n^2)

# S.C = O(1) + O(n) or O(1) 
## here O(n) is ans and ans is also returned, so S.C can be O(1)
## we didn't use any extra space(append), so S.C is O(1)

def next_greater_arr(arr):
    ans = [-1] * len(arr)
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] > arr[i]:
                ans[i] = arr[j]
                break
        
    return ans
print(next_greater_arr([1,6,3,4,2,7,0]))

#Brute Force Solution 2
# T.C = O(n*(n+1)/2) = O(n^2)
# S.C = O(1)

def next_greater_arr1(arr):

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] > arr[i]:
                arr[i] = arr[j]
                break
        else:
            arr[i] = -1
    return arr
print(next_greater_arr1([1,6,3,4,2,7,0]))





## Optimal solution
#T.C. = O(2n) = O(n)
#S.C. = O(n-1) = O(n)
def next_greater_arr2(arr):
    stack = []
    ans = [-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans

print(next_greater_arr2([1,6,3,4,2,7,0]))

