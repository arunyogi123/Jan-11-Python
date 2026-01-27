import random

random_num = random.randint(10,20)
total_game_played = 1
user_point = 0
computer_point = 0
game_point = 50
print(random_num)

count = 0
while True:

    if user_point == 50 or computer_point == 50:
        print("Game Over")
        if user_point == 50:
            print("User win by ", user_point-computer_point , "point")

        elif(computer_point==50):
            print("computer win by ", computer_point-user_point , "point")
        break
    
    count = count +1
    num = int(input("enter a number "))
    if random_num == num:
        user_point = user_point +10
        print("Number match in ", count, "times")
        play_again = input("Do you want to play again")
        if play_again == "y":
            random_num = random.randint(10,20)
            total_game_played = total_game_played +1
            print("new....", random_num)
            count = 0
            print("lets play a game")
        else:
            print("total game played = ", total_game_played)
            break
    else:
        computer_point = computer_point+5
        print("Try again")