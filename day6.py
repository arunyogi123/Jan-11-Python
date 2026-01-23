#Membership operator

#in , not in
a=[1,2,3,4,5,6,7]
print(10 in a)
print(10 not in a)

#is, is not (==)
a=2
print(a is None)
#"" vs None

for i in range(11):
    if i%2==0:
        print(f'{i} is even')
print("-------------------------"*40)

a=[1,2,3,4,5,'arun',2,34,5] 
for i in range(len(a)):
    print(a[i])     

    
a=[1,2,3,"Hello",3,4,5,"Arun",2,3]
for i in a:
    if isinstance(i,str):
    
        continue
    print(i)
    
print("-------------------------"*10)
for i in range(1,4):
    for j in range(5,8):
        if j==6:
            break
        print(i,j)
     