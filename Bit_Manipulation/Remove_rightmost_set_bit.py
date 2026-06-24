#remove the last set bit in binary representation

#optimal solution

def remove_rightmost_set_bit(n):
    n = n&(n-1)
    print("removed")
    print(f"n = {n}")
remove_rightmost_set_bit(25)