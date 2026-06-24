#a array contains duplicates value excepts one number

#optimal solution(using BIT manipulation)

def find_single_ele(list):
    ans = 0
    for i in list:
        ans ^= i
    return ans
print(find_single_ele([1,2,3,2,4,5,4,1,5]))



#Brute Force solution 
#find frequency first and store in dictionary


def find_single_ele2(list):
    dic = {}
    for ele in list:
        dic[ele] = dic.get(ele,0) +1
    for key in dic:
        if dic[key] == 1:
            return key
print(find_single_ele2([1,2,3,2,4,5,4,1,5]))


