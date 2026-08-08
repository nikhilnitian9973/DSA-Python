# Given two arrays, val[] and wt[] , representing the values and weights of items,
#  and an integer capacity representing the maximum weight a knapsack can hold,
#  determine the maximum total value that can be achieved by putting items in the knapsack. 
# You are allowed to break items into fractions if necessary.
# Return the maximum value as a double, rounded to 6 decimal places



#### Optimal Solution
#T.C = O(n) + O(nlogn) +O(n) = O(nlogn)
#S.C = O(n)

def fractionalKnapsack(val, wt, capacity):
    #code here
    # val_wt = list(zip(val,wt))
    val_wt = []
    for i in range(len(val)):
        val_wt.append((val[i],wt[i])) 
    key = lambda x: x[0]/x[1]
    val_wt.sort(key = key,reverse=True) # val_wt.sort(key = lambda x: x[0]/x[1],reverse=True)       
    sum = 0
    for i in range(len(val_wt)):
        if capacity == 0:
            break
        if val_wt[i][1] <=capacity:
            sum += val_wt[i][0]
            capacity -= val_wt[i][1]
        else:
            sum += val_wt[i][0]  *capacity / val_wt[i][1]
            capacity = 0
    return sum

val = [10,40,60,100]
wt = [20,40,80,90]
capacity  = 100
print(fractionalKnapsack(val,wt,capacity))