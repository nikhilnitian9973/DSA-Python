#using recursion

class Solution:
    def isPalindrome(self, s, l = 0,r = len(s)-1):
        if l>r:
            return True
        # code here
        
        return s[l] == s[r] and self.isPalindrome(s,l+1,r-1)
        
s = Solution()
string = "abccba"
result = s.isPalindrome(string)
print(result)