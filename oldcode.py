'''
n= 0
while n > -1:
    print(str(n) + '%')
    n = n + 1
    if n == 100:
        print('100%')
        break
'''

import random

'''
x = random.randint(1, 10)
y = 0
cnt = 0
con = 'y'
while con == 'y':
    while y != x:
        y = input('Write your num: ')
        y = int(y)
        if y > x:
            print('Your number is larger than answer , try again !!')
        elif y < x:
            print('Your number is smaller than answer , try again !!')
        cnt = int(cnt)
        cnt = cnt + 1
    print('You win !!!!')
    cnt = str(cnt)
    print('You tried >> ' + cnt + ' << times to win this game.\n')
    y = 0
    con = input('Do you want to continue ??(y/n)')
'''

'''
x = input('Write the num: ')
x = int(x)
y = 0
cnt = 0
while y != x:
    y = random.randint(1,100)
    y = int(y)
    print(y)
    cnt = cnt + 1
    if cnt > 3 :
        print('ha ha ha you loose your chance PC jan . . . ')
        break
    else:
        continue
print('PC win !!!!')
cnt = str(cnt)
print('Pc tried >> ' + cnt + ' << times to win this game.\n')
'''

# cnt = 0
# word = 'my stringg'
# l = list(word)
# # print(l)
# for l in word :
#     print(l)
# if word == 'g':
#     cnt = cnt +1
# print('word count:',cnt)
#
# string = 'hello yaser this is python'
# count = 0
# for letter in string:
#     if letter == 'h':
#         count = count + 1
# a = len(string)
# print('word count h:' + str(count) + ' |count len :' + str(a) )
# a = 'Yaser'.lower().find('y')
# print(a)
# name = 'yaser'
# age = 23
# b = print('hello %s with age %s' % (name.upper(),age))
# print(b)
# a = a.split()
# print(a)
# b1 = ' '.join(a[0:3])
# b2 = ' '.join(a[3:5])
# b3 = ''.join(a[5])
# print(b1 + b2 + ' ' + b3)
# a = [1, 2, 3]
# b = [1, 2, 3]
# a[0] = ' yas'
# print(a , b)
# a = 'hello world ! i am yaser'
# counter = dict()
# for letter in a:
#     print(letter)
#     if letter in counter:
#         counter[letter] += 1
#     else:
#         counter[letter] = 1
# print(counter)
# for this in list(counter.keys()):
#     print('%s appeared %s times' % (this,counter[this]))
# for letter in a:
#     print(letter)
#     counter[letter] = counter.get(letter, 0) + 1
# print(counter)
# for this in list(counter.keys()):
#     print('%s appeared %s times' % (this, counter[this]))

# file = open('test')
# content = file.read()
# print(content)
# file.close()
# counter = sum = 0
# fin = open('test')
# for line in fin:
#     print(line.strip())
#     counter += 1
#     this_num = float(line.strip())
#     sum = sum + this_num
#     avg = sum / counter
# print(counter, int(sum), int(avg))
# fin.close()
# fin = open('test', 'w')
# fin.write(str(avg))
# fin.close()


# import csv
#
# with open('test.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print(row)
#          id = row[0]
#         for grade in row[0:]:
#             print(grade)
# a=min([sum([11, 22]), max(abs(-30), 2)])
# print(a)
# m = lambda x: x * 2
# # print(m(3))
# a = [(3, 4), (7, 1), (5, 9), (2, 2)]
# a.sort(key=lambda x: x[1])
# print(a)
# listt = [1, 2, 35, 4]
# s = list(map(lambda x: 'big' if x > 10 else 'small', listt))
# o = list(filter(lambda x: x > 3,listt))
# print(s)
# print(o)


# def first():
#     for i in range(1, 3000000):
#         yield i
# for i in first():
#     print(i)


# def firstn(n):
#     num = 0
#     while (num < n):
#         yield num
#         num += 1
#
#
# for i in firstn(10000000):
#     print(i)


# class Person:
#     count = 0
#
#     def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       Person.count = Person.count + 1
#     def get_name(self):
#         print('name is: %s' %self.name)
#         print('age is: %s' %self.age)
#     def r_cnt(self):
#         return (Person.count)
# yaser = Person('Yaser',23)
# yaser.get_name()
# print(yaser.r_cnt())


# class Computer:
#     def __init__(self, hard, cpu, ram):
#         self.hard = hard
#         self.ram = ram
#         self.cpu = cpu
#
#     def value(self):
#         return self.hard * 3 + self.ram * 2 + self.cpu * 4
#
#
# class Laptop(Computer):
#     def value(self):
#         return self.hard * 3 + self.ram * 2 + self.cpu * 4 + self.size
#
#
# pc1 = Computer(1.2, 2.5, 0.8)
# print(pc1.value())
#
# laptop1 = Laptop(2, 2.5, 1)
# laptop1.size = 14
# print(laptop1.value())

#
# class Device:
#     cnt = 0
#
#     def __init__(self, ip, mac, name):
#         self.ip = ip
#         self.mac_address = mac
#         self.name = name
#         Device.cnt += 1
#         result = ping the device
#         if result :
#             self.status = 'active'
#         else :
#             self.status = 'unkown'
#
# class TV(Device):
#     def turn_on(self):
#         #connect to self.ip and turn on
#         print("Tv is on")
#     def turn_off(self):
#         print("Tv is off")
# class Thermo(Device):
#     def get_degree(self):
#         return result