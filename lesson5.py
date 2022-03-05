# coding = utf-8
from functools import reduce
# task1
cnt = 0
for i in range(1,101):
    if i % 3 == 0:
        cnt += i
print(cnt)

cnt = reduce(lambda x,y:x+y,[i for i in range(1,101) if i % 3 ==0])
print(cnt)

# task2
height1 = int(input('请输入高度(整数):'))
weight1 = int(input('请输入宽度(整数):'))
for i in range(height1):
    for j in range(weight1):
        print('*',end = ' ')
    print()

# task3
for i in range(1,10):
    for j in range(1,i + 1):
        print('%d X %d = %d' % (i,j,i*j))

# task4
nums = [23,45,8,13,50,43,21]
sum1 = 0
for i in nums:
    sum1 += i
    if sum1 > 100:
        break
print(sum1)