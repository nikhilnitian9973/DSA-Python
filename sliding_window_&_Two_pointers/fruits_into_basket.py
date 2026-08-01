

#Brute Force Solution
#T.C = O(n*(n+1)/2) = O(n^2)
#S.C = O(1)

def fruits_into_basket(fruits):
    maxi = 0
    for i in range(len(fruits)):
        my_set = set()
        for j in range(i,len(fruits)):
            if fruits[j] not in my_set:
                my_set.add(fruits[j])
            else:
                break
            maxi = max(maxi,j-i+1)
    return maxi
fruits = [1,2,4,2,4,6,4,3,2]
print(fruits_into_basket(fruits))

#better solution
#T.C =  O(n)+O(n) = O(n)
#S.C = O(1)
def fruits_into_basket1(fruits):
    maxi = 0
    left  = 0
    right = 0
    my_dic = {}

    while right <len(fruits):
        my_dic[fruits[right]] = my_dic.get(fruits[right],0)+1
        while len(my_dic) >2:
            my_dic[fruits[left]] -=1
            if my_dic[fruits[left]] == 0:
                my_dic.pop(fruits[left])
            left +=1
        

        maxi= max(maxi,right-left +1)
        right +=1
    return maxi
print(fruits_into_basket1(fruits))

#Optimal solution
#T.C =  O(n)+O(n) = O(n)
#S.C = O(1)
def fruits_into_basket2(fruits):
    maxi = 0
    left  = 0
    right = 0   
    my_dic = {}

    while right <len(fruits):
        my_dic[fruits[right]] = my_dic.get(fruits[right],0)+1
        if len(my_dic) >2:
            my_dic[fruits[left]] -=1
            if my_dic[fruits[left]] == 0:
                my_dic.pop(fruits[left])
            left +=1
        

        maxi= max(maxi,right-left +1)
        right +=1
    return maxi
print(fruits_into_basket2(fruits))