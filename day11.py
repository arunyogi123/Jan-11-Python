# def  user_info(fname, lname):
#      return fname, lname

# print(user_info(lname="yogi", fname="arun"))

# def add(*a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     return sum
# print(add(1,2,3,4,5,6,7))
# print(add(111,222))


# def check_number(*a):
#     a=list(a)
#     a.sort
#     print(a)
#     return a[-2]
# print(check_number(1,2,3,4,5,6))

# def number(*a):
#     data=set(a)
#     return list(data)
# print(number(1,1,1,2,3,4,5))


def data_type(*a):
    count_int=0
    count_str=0
    count_float=0
    other=0
    for i in a:
        if isinstance(i,int):
            count_int=count_int+1
    
           
        elif isinstance(i,str):
            count_str=count_str+1
            
        elif isinstance(i,float):
             count_float=count_float+1
             
        else:
            other=other+1
            
    return{
        "int":count_int,
        "str":count_str,
        "float":count_float,
        "other":other
    }

    
print(data_type(1,2,2.4,"arun",[1,2]))
            
            




