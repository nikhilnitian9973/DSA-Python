#Bruteforce solution

def convert_int_to_binary(num):
    if num == 0:
        return "0"
    result = ""
    while num != 0:
        result = str(num %2) + result
        num //= 2
    return result
print(convert_int_to_binary(13))