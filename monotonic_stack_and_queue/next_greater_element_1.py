






#Brute Force solution

def next_greater_arr(arr):
    # ans = [-1] * len(arr)  (we can use this also)
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] > arr[i]:
                arr[i] = arr[j]
                break
        else:
            arr[i] = -1
    return arr
print(next_greater_arr([1,6,3,4,2,7,0]))
























## Optimal solution
#T.C. = 
def next_greater_ele_arr(arr):
    stack = []
    ans = [-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(arr[i])
    return ans

print(next_greater_ele_arr([1,6,3,4,2,7,0]))