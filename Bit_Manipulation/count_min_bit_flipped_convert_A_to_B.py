#count minimum number of bits to be flipped to convert A to B

#optimal solution

def min_num_flipped(start,goal):
    a = start^goal
    ans = 0
    for i in range(0,32):
        if a & (1<<i) != 0:
            ans +=1
    return ans
print(min_num_flipped(25,34
                      ))
    