
#Optimal Solution
#T.C = O(2*2n) = O(n)
#S.C = O(n)

def next_greater_arr(arr):
    n = len(arr)
    stack = []
    ans = [-1]*n
    for i in range(2*n-1,-1,-1):
        while stack and stack[-1] <= arr[i%n]:
            stack.pop()
        if i <n:
            if stack:
                ans[i] = stack[-1]
        stack.append(arr[i%n])
    return ans
