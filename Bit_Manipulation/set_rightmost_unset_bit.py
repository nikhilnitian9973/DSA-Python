#set the last unset bit

#optimal solution

def set_rightmost_unset_bit(n):
    n = n|(n+1)
    print("setted rightmost unset bit")
    print(f"n = {n}")
set_rightmost_unset_bit(25)
