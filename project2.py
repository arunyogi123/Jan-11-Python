import streamlit as st
import requests
import random


st.title("Hello from python project")
a = 2 +2
st.text(a)


# url = "https://www.onlinekhabar.com/smtm/home/top-gainers/1d"
# r = requests.get(url=url)
# if r.status_code == 200:
#     data = r.json()['response']
#     for i in data:
#         st.text(i['ticker_name'])
# else:
#     print("failure")


# url = "https://www.onlinekhabar.com/wp-json/okapi/v1/taja-updates?limit=9"
# r = requests.get(url=url)
# if r.status_code == 200:
#     result = r.json()

#     for i in result["data"]["news"]:
#         final_result = f"""{i['title']} - {i['link']}"""
#         st.text(final_result)

# else:
#     print("failure from server")


# data = st.number_input("Enter a number", step=1)
# result = f"enter number is {data} "
# if data:
#     st.text(result)
#     st.success(result)


# data = st.date_input("Date ")
# data2 = st.button("Play Again")


random_number, nepsedata, news = st.tabs(["Game", "Nepse", "News"])




with random_number:
    st.text("this is random number game")
    # random_num = random.randint(10,20)
    # total_game_played = 1
    # user_point = 0
    # computer_point = 0
    # count = 0
    # game_point = 50
    # print(random_num)
    # num = st.number_input("Enter a number" ,key=f"uni{count}", step=1)
    # if num:

    #     while True:
    #         if user_point == 50 or computer_point == 50:
    #             print("Game Over")
    #             if user_point == 50:
    #                 print("User win by ", user_point-computer_point , "point")

    #             elif(computer_point==50):
    #                 print("computer win by ", computer_point-user_point , "point")
    #             break

    #         count = count +1
    #         if random_num == num:
    #             user_point = user_point +10
    #             print("Number match in ", count, "times")
    #             play_again = input("Do you want to play again")
    #             if play_again == "y":
    #                 random_num = random.randint(10,20)
    #                 total_game_played = total_game_played +1
    #                 print("new....", random_num)
    #                 count = 0
    #                 print("lets play a game")
    #             else:
    #                 print("total game played = ", total_game_played)
    #                 break
    #         else:
    #             computer_point = computer_point+5
    #             print("Try again")



with nepsedata:
    url = "https://www.onlinekhabar.com/smtm/home/top-gainers/1d"
    r = requests.get(url=url)
    if r.status_code == 200:
        data = r.json()['response']
        st.data_editor(data)

    else:
        print("failure")

with news:
    st.text("this is news")