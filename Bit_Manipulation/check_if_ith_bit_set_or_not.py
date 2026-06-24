#problem: check if ith bit is set or not

#optimal solution
def check(n,i):
    if (n & (1<<(i-1))) != 0:
        return "SET"
    else:
        return "NOT SET"
print(check(25,3))