#count all set bit in all 1 to n numbers
#n = 4 -->> 001,010,011,100  -->>  count = 1+1+2+1 = 5
#no. of set bit 1 to 4 is : 5


#solution (T.C. -> O(n), S.C. -> O(1))

def count_set_bit(n):
    count = 0
    for num in range(1,n+1):
        for i in range(32):
            if num & (1<<i) != 0:
                count +=1
    return count

print(count_set_bit(4))


#Solution (T.C. -> O(log n), S.C. -> 0(1))

def count_set_bit2(n):
    count = 0
    bit = 1
    while bit <= n:
        cycle = 2*bit
        full_cycles = n // cycle
        remainder = n % cycle

        count += full_cycles*bit
        count += max(0,remainder -bit +1)
        bit *=2

    return count
print(count_set_bit2(4))