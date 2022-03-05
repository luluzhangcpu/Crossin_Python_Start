# coding = utf-8

# task1
money = 88
if money > 100:
    print('rich')
else:
    print('poor')

# task2
bingo = False
if bingo == False:
    print(True) # 输出 True
else:
    print(False)

b = 3
if b - 3:
    print(True)
else:
    print(False) # 输出 False

x = input('请输入内容') # 若输入内容了，输出 True，否则 False
if x:
    print(True)
else:
    print(False)

a = True
b = not a
print(b) # F
print(not b) # T
print(a == b) # F
print(a != b) # T
print(a and b) # F
print(a or b) # T
print(1 < 2 and b == True) # F

# task3
sg = float(input('请输入你的身高(米):'))
tz = float(input('请输入您的体重(公斤):'))
bmi = tz / (sg ** 2)
if bmi < 18.5:
    print('体重偏轻')
elif bmi < 24:
    print('体重正常')
else:
    print('体重偏重')