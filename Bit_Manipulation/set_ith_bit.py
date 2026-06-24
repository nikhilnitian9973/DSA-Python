#problem: set the ith bit in binary representation of a number

#Optimal solution

def set_bit(n,i):
    n = n|(1<<(i-1))
    print("n have been changed")
    print(f"n = {n}")
set_bit(25,2)