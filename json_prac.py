# JSON is commonly used with data APIS. Here's how we can parse JSON into Python Dictionary

import json

# sample json

userJSON = '{"first_name": "John", "Last_name": "Doe", "age": "30"}'

user = json.loads(userJSON)

print(user) # print dic

#get first name
print(user['first_name'])

# turn a dict into json
car = {'make': 'Ford', 'model' : 'Mustang', 'year': 1970}

carJSON =json.dumps(car)

print(carJSON)