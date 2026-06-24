#problem: Toggle ith bit

#optimal solution

def toggle_bit(n,i):
    n = n ^ (1<<(i-1))
    print("Toggled ith bit")
    print(f"n = {n}")
toggle_bit(25,5)