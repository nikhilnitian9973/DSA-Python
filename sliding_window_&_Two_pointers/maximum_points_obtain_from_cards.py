

def maximum_points(cardPoints,k):
    n = len(cardPoints)
    if k == n:
        return sum(cardPoints)
    window_size = n-k
    current_window = cardPoints[:window_size]
    current_window_sum = sum(current_window)
    mini = sum(current_window)
    right = current_size
    while right <n:
        current_window_sum += cardPoints[right]-cardPoints[right-window_size]
        mini= min(mini,current_window_sum)
        right +=1
    return sum(cardPoints) - mini

cardPoints,k = [1,2,3,4,5,6,1],3
print(maximum_points(cardPoints,k))
