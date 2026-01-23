# membership opeartor

# in , not in
a = [1,2,3,5,5,6,7]
print(10 not in a)


#is , is not (==)
a = ""
print(a is None)
# "" vs None



'''
for i in <list, string, dict>:
    print(i)
    print(i)
    print(i)
    print(i)
    print(i)
    print(i)
    print(i)
    print(i)

'''



for i in "broadway":
    print(i)



for i in [1,2,3,4,5,6,7,8,9,10]:
    if (i%2==0):
        print(f'{i} is even')
    else:
        print(f'{i} is odd')



# range(1,10,1)
for i in range(1,10,1):
    print(i)

for i in range(10,1,-1):
    print(i)




print("------------")
a = [1,2,3,"test",5,6,7]
print(".....",len(a))

for i in a:
    print(i)


print("........")
for i in range(len(a)):
    print(a[i])



print("+++++++++++++++++++")
a = [1,2,3,"test",5,6,7]
for i in a:
    if i == "test":
        break
    print(i)

a = [1,2,3,"test",5,6,7]
for i in a:
    if i == "test":
        continue
    print(i)

a = [1,2,"nepal",3,"test",5,6,7, "hello"]
for i in a :
    if isinstance(i, str):
        continue
    print(i)

print("===================")

for i in range(1,4):
    for j in range(5,8):
        if j == 6:
            break
        print(i,j)