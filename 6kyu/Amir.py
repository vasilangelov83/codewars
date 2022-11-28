def repeating_element(arr, num):
    new_list = []
    for element in arr:

        if new_list.count(element) < num:
            new_list.append(element)
    return print(new_list)




repeating_element([1,2,3,1,2,1,2,3],2)