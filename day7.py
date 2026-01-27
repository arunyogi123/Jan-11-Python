#random
import random

print(random.random())

num = random.randint(10,20)
print(num)

for i in range(10,16):
    user_input = int(input("Enter a number: "))
    if user_input == num:
        print("Number guessed successfully" , i)
        break
    else:
        print("Try again")

a = [1,2,3,4,"sudan",True, 4.6,None]
print(random.choice(a))


import random
num = random.randint(10,20)
print(num)
count=0
total_game=1
while True:
     num2=int(input("enter the guess_num"))
     count=count+1
     if num2==num:
         print('num matches in',count)
        
       
         play_again=input("wanna play again")
         if play_again=="y":
             num = random.randint(10,20)    
             total_game=total_game+1 
             print("new num =",num)
             count=0 
             print("lets go")
        
         else:
             print("total game played =",total_game)
             break
    
    
# i=1
# while i<=10:
#     print(f' {i} ')
#     i=i+1

        