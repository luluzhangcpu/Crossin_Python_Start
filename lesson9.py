# coding = utf-8

from math import pi as math_pi
from random import randint

# task1
r = 20
s = math_pi * r * r
print(s)

# task2
b = 0
for i in range(10):
    a = randint(1,100)
    if a > b:
        b = a
print(b)

# task3
a = randint(1,100)
h = True
cnt = 0
while h:
    b = int(input('请在 1～100 间输入一个整数：'))
    if a > b:
        print('太小了，再猜猜看')
        h = True
    elif a < b:
        print('太大了，再猜猜看')
        h = True
    else:
        h = False
    cnt += 1
print('太好了，恭喜你答对了！共计猜 %d 轮' % cnt)