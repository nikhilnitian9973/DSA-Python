#problem: clear ith bit

#optimal solution

def clear_bit(n,i):
    n = n & ~(1<<(i-1))
    print("ith bit cleared")
    print(f"n = {n}")
clear_bit(25,5)

