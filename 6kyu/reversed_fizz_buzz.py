
def reverse_fizzbuzz(string):

    list_of_num = [int(x) if x.isdigit() else x for x in string.split(" ")]

    for x in list_of_num:
        if type(x) is int:
            result =[i[0] for i in list(enumerate(list_of_num,start=x - list_of_num.index(x)))]
        elif list_of_num == ["Fizz","Buzz"]:
            result = [9,10]
        elif list_of_num == ['Buzz','Fizz']:
            result = [5,6]
        elif list_of_num == ['Fizz']:
            result = [3]
        elif list_of_num == ['Buzz']:
            result = [5]
        elif list_of_num == ['FizzBuzz']:
            result = [15]



    return  result
print(reverse_fizzbuzz("1 2 Fizz 4 Buzz"))
print(reverse_fizzbuzz("Fizz 688 689 FizzBuzz"))
print(reverse_fizzbuzz("Fizz Buzz"))