#leetcode question 3

# Brute Solution
# T.C = O(n(n+1)/2) = O(n^2)
# S.C = O(n)

def longest_substring(s):
    maxi= 0
    for i in range(len(s)):
        my_set = set()
        for j in range(i,len(s)):
            if s[j] in my_set:
                break
            maxi = max(maxi,j-i+1)
            my_set.add(s[j])
    return maxi
s = "aebdceabhj"
print(longest_substring(s))

#optimal solution
#T.C =  O(n)+O(n) = O(n)
#S.C = O(n)

def longest_substring1(s):
    dic = {}
    left = 0
    right = 0
    maxi = 0
    while right <len(s):
        if s[right] in dic:
            left = max(left,dic[s[right]]+1)
        maxi = max(maxi,right-left+1)
        dic[s[right]] = right
        right +=1
    return maxi

print(longest_substring1(s))




