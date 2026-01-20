a = [1,2,3,4,5,6]
print(type(a))
print(a)


a = [1,2,3,4,"sudan",True, 4.6,None]
print(a[4])
print(a[-1])
# print(a[10])

print(len(a))


# slicing
print(a[0:4])
print(a[:6])
print(a[4:])
print(a[:])


# adding data in list
data = ["hello","namaste",2,1,1,1,1,2,3,1,2]
# append
# insert
# extends
# concat



# append
data.append("append command")
data.append("append command2")


# insert
data.insert(7,"sudan")
# data.insert(7000,"sudan") add data in last of list

print(data)

# extends

a = [1,2,3,4,5]
b = [6,7,8,9,0]
b.extend(a)
a.extend(b)

print(a)


# concat
c = [1,2]
d = [3,4]
e = c+d
print(e)
print(c,d)



# del
# remove
# pop
# clear
print("-----"*30)
data = [1,2,3,4,1,2,3]
del data[0]

# remove command used for deleting value
data.remove(4)
data.remove(2)


print(data)

# pop
data = [1,2,3,4,5,6,7,8]
print(data)
remove_data = data.pop()
print("Remove data is ", remove_data)


# clear
data.clear()
print(data)