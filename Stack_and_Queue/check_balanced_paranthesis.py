# check if a string is balanced or not
# leetcode Question 20

def is_balanced_paranthesis(s):
    stack = []
    check = False
    for i in s:
        if i in "{([":
            stack.append(i)
        else:
            if not stack:
                return False
            if (i == "}" and stack[-1] == "{") or \
                (i == "(" and stack[-1]== ")") or \
                    (i=="[" and stack[-1]=="]"):
                stack.pop()
                
            else:

                return False
    if not stack:
        check = True
    return check

print(is_balanced_paranthesis("[)]"))