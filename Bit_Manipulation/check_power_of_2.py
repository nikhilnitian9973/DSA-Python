#check if a number is power of 2 or not

#optimal solution

def check_power_2(n):
    if n&(n-1) == 0:
        return "Power of 2"
    else:
        return "not powe of 2"
print(check_power_2(1024))