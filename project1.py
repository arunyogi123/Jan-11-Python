import requests

url = "https://www.onlinekhabar.com/wp-json/okapi/v1/taja-updates?limit=9"
r = requests.get(url=url)
if r.status_code == 200:
    result = r.json()
    # print(type(result))
    # print(result.keys())
    # print(type(result['data']))
    # print(result['data'].keys())
    # print(result['data']['news'])
    # print(type(result['data']['news']))
    # print(result['data']['news'][0])
    for i in result["data"]["news"]:
        final_result = f"""{i['title']} - {i['link']}"""
        print(final_result)

else:
    print("failure from server")





url = "https://www.onlinekhabar.com/smtm/home/top-gainers/1d"
r = requests.get(url=url)
if r.status_code == 200:
    data = r.json()['response']
    for i in data:
        print(i['ticker_name'] , i['prices'])
else:
    print("failure")