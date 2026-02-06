def greet():
    a = 1
    print(a)
    n = 11
    if n%2==0:
        print("even")
    else:
        print("Odd")
    return 1,9
    return ("Namaste","hello")
    print("this is testing")
    SingleAddressHeaderfad
    adaptasd
    asdictasd
    assertda
    set_debugasd





# print(type(greet()))



def user_info():
    fname = "sudan"
    lname = "sharma"
    return fname, lname


# print(user_info())



def add_list_data():
    a = [100,2,3,4,5,6,7]
    sum_list = 0
    for i in a:
        sum_list = sum_list +i
    return sum_list






print(add_list_data())


def add(a,b):
    return a+b

print(add(10,20))
# print(add(12343,1234))
# print(add(1433,1243))
# print(add(1433,1432))

def check_number(n,n1,n2,n3):
    if n>0:
        return("positive")
    elif(n<0):
        return("Negtive")
    else:
        return("wrong input")

print(check_number(1,1,1,1))



def user_info(fname, lname):
    return fname, lname


print(user_info(lname=['sharma'],fname=[1,2,3,4]))



def test(*args):

    sum_list = 0
    for i in args:
        sum_list = sum_list +i
    return sum_list

print(test(1,2))
print(test(1,2,3))
print(test(10,20,30,40))
print(test())



def check_largest_num(*a):
    a=list(a)
    a.sort()
    print(a)
    return a[-2]


print(check_largest_num(5,10,75,2))
print(check_largest_num(60,50,78,40))


# Write a Python program that defines a function using *args to accept any number of integers and:

# Remove duplicate values

# Display the final unique list


def removeDup(*args):
    new_list = []
    for i in args:
        if i in new_list:
            continue
        else:
            new_list.append(i)

    return new_list


print(removeDup(1,1,1,1,2,2,2,2,3,3,4,5,6))




def removeDups(*args):
    data = set(args)
    return list(data)


print(removeDups(1,1,1,1,2,2,2,2,3,3,4,5,6))



def longest_string(*args):
    length = 0
    longest_data = ""

    for i in args:
        data_length = len(i)
        if data_length >= length:
            length = data_length
            longest_data = i
    return longest_data

print(longest_string("apple","orange","test","testing"))



def count_datatype(*args):
    data = {
        "int":0,
        "str":0,
        "float":0,
        "other":0
    }
    for i in args:
        if isinstance(i,int):
            data['int'] = data['int']+1
        elif isinstance(i, str):
            data['str'] = data['str']+1
        elif isinstance(i,float):
            data['float'] = data['float']+1
        else:
            data['other'] = data['other']+1


    return data


print(count_datatype(1,2,3,"hello",4.1, [1,23]))


# int:3
# str:1
# float 1
# other: 1
