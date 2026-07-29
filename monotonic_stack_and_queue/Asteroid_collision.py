# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


##Optimal Solution
# T.C = 
# S.C = O(n)

def asteroid_collision(asteroids):
    stack = []
    for i in range(len(asteroids)):
        if asteroids[i] >0:
            stack.append(asteroids[i])
        else:
            while stack and stack[-1]>0 and stack[-1] < abs(asteroids[i]):
                stack.pop()
            if not stack or stack[-1]<0:
                stack.append(asteroids[i])
            elif stack and stack[-1] + asteroids[i] == 0:
                stack.pop()
    return stack

print(asteroid_collision([3,5,-6,2,-1,4]))