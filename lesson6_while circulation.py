from random import randint
# task1
h = True
a = randint(1,100)
while h:
    b = int(input('请输入一个1～100间的整数:'))
    if b < a:
        print('太小了，再猜猜看')
        h = True
    elif b > a:
        print('太大了，再猜猜看')
        h = True
    else:
        h = False
print('恭喜你，答对了！')

# task2
cnt = 0
while cnt < 10:
    cnt += 1
    if cnt == 4 or cnt == 5:
        continue
    print(cnt)

# task3
cnt = 0
s = 0
while cnt < 100:
    cnt += 1
    if cnt % 3 == 0:
        s += cnt
print(s)
