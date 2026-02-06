# tuple set

# dict {} and key value
# set {}
# tuple = ()

tup_data = (1,2,3,4,5,6,7,8)
print(type(tup_data))

list_data = list(tup_data)
print(type(list_data))
print(list_data.pop())

tup_data = tuple(list_data)
print(tup_data)



set_data = {"sudan","1","2",1,2,1,11,1,1,1,1,1,1,1,1,1,1,4, "testing"}
data = list(set_data)

print(set_data)


for i in set_data:
    print(i)



a = [1,1,1,1,2,2,2,2,2]
data = set(a)
a = list(data)
a.remove(1)
print(a)