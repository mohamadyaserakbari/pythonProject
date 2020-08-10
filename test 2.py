# from itertools import accumulate
#
# a = ["a","b","c","d"]
# print(list(accumulate(a)))


# from itertools import groupby

#
# a = [1, 2, 3, 4]
# go = groupby(a, key=lambda x: x < 3)
# for key, value in go:
#     print(key, list(value))

# person = [
#     {'name': 'Yaser', 'age': 23},
#     {'name': 'Amin', 'age': 20},
#     {'name': 'Zahra', 'age': 20},
#     {'name': 'Akram', 'age': 27}
# ]
# go = groupby(person, lambda x: x['age'])
# for key, value in go:
#     print(key, list(value))

#
# from itertools import count,repeat,cycle
# from time import sleep
# for i in count(10):
#     print(i)
#     sleep(1)
#     if i == 100:
#         print("time is over!!")
#         exit()
#
# from functools import reduce
#
# a = [1, 2, 3, 4, 5, 6]
# b = reduce(lambda x, y: x * y, a)
# print(b)


import json


# person = {
#     "name": "Yaser",
#     "age": 23,
#     "city": "Qom",
#     "hasChildern": False,
#     "title": [
#         "engineer",
#         "Python Developer"
#     ]
# }
#
# personjson = json.dumps(person, indent=2, sort_keys=True)
# with open('person.json', 'w+') as file:
#     json.dump(person, file,indent=3)
# with open('person.json', 'r') as file:
#     person =  json.load(file)
#     print(person)

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user = User("Yaser", 23)
#
#
# def encode_user(o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
#     else:
#         raise TypeError('This object doesnt serialize')
#
#
# user_json = json.dumps(user , default=encode_user)
# print(user_json)




