#return a power set in list data type

#optimal solution

def power_set_of(list):
    len_list = len(list)
    len_power_set = 1<<len_list
    result = []
    for num in range(len_power_set):
        lst = []
        for i in range(len_list):
            if num & (1<<i) != 0:
                lst.append(list[i])
        result.append(lst)
    return result
print(power_set_of([1,2,3,4]))
