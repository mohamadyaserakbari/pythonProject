'''x = input('Please give your age: ' + ' ')
y = int(x)
if y == 8:
    print(y * 8)
elif y > 8:
    print(y * 2)
elif y < 8:
    print(y * 0)
else:
    print('Use int for question . . . ')
'''
'''
import random
x = random.randint(1, 1000)
y = random.randint(1, 1000)
z = random.randint(1, 1000)
w = random.randint(1, 1000)
xx = int(x)
yy = int(y)
zz = int(z)
ww = int(w)
print(xx, yy, zz, ww)
'''

'''
def salambye(n1,n2):
    print('salam', n1)
    print('Bye Bye', n2)
    jam = n1 + n2
    print(jam)
x = input('write your first num: ')
y = input('write your second num: ')
salambye(int(x),int(y))
'''


def salambye(n1, n2):
    jam = n1 * n2
    if n1 > 8:
        print('Dont work too much!!!')
    else:
        return jam


x = input('write your hour: ')
y = input('write your salary: ')
z = salambye(int(x), int(y))
print('Your salary is: ' + str(z))
