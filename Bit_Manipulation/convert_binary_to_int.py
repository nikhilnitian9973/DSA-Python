#problem: convert binary to integer

#brute force solution

def convert_binary_to_int(b):
    num = 0
    for i in range(0,len(b)):
        num += int(b[len(b)-i-1])*(1<<i)
    return num
print(convert_binary_to_int("1101"))