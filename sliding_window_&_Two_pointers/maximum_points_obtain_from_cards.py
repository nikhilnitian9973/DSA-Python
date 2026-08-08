
#Optimal SOlution 1
#T.C = O(n)
#S.C = O(1)
def maximum_points(cardPoints,k):
    n = len(cardPoints)
    if k == n:
        return sum(cardPoints)
    window_size = n-k
    current_window = cardPoints[:window_size]
    current_window_sum = sum(current_window)
    mini = sum(current_window)
    right = window_size
    while right <n:
        current_window_sum += cardPoints[right]-cardPoints[right-window_size]
        mini= min(mini,current_window_sum)
        right +=1
    return sum(cardPoints) - mini

cardPoints,k = [1,2,3,4,5,6,1],3
print(maximum_points(cardPoints,k))


#Optimal SOlution 2
#T.C = O(n)
#S.C = O(1)

def maximum_points2(cardPoints,k):
    n = len(cardPoints)
    if n ==k:
        return sum(cardPoints)
    left_sum,right_sum = 0,0
    for i in range(k):
        left_sum += cardPoints[i]
    maxi = left_sum
    i = k
    j = -1
    while i:
        left_sum -= cardPoints[i-1]
        right_sum += cardPoints[j]
        maxi = max(maxi,left_sum + right_sum)
        i-=1
        j-=1
    return maxi
print(maximum_points2(cardPoints,k))
    
