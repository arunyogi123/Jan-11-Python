# a={} and key value pair => dict

a={
    'name':"arun",
    'address':"Kathmandu",
    'age':20
}

print(type(a))
print(a)

print(a['name'])

print(len(a))

print(a.keys())
print(a.values())


#a['address']="Kupondole"  #UPDATE
#a['phone']=90909090

a.update({'address':'Nepal',"phone":90909090})
print(a)


data={
    'name':'Balen Shah',
    'address':'Jhapa 5',
    'winner':True,
    'post':['Ex-mayor','Rapper','PM']
}

print(data['post'][0])

#del
#pop()
#popitem()
#clear

del data['winner']

a=data.pop('name')
print(data)
print(a)

#popitem
data.popitem()
print(data)

#clear
data.clear()
print(data)

data={
    'name':'Balen Shah',
    'address':'Jhapa 5',
    'winner':True,
    'post':['Ex-mayor','Rapper','PM']
}

print(data.get('roles'))

data = {
    "namse":"Hari",
    "phone":[
        {
            "number":980,
            "type":"Ncell"
        },
        {
            "number":9844,
            "type":"NTC"
        }
    ]
}

if "namse" in data:
    data["name"]=data["namse"]
print(f'{data["name"]} {data["phone"][0]["type"]} number is {data["phone"][0]["number"]}')

#print(f'{data["name"]} {data["phone"][1]["type"]} number is {data["phone"][1]["number"]}')