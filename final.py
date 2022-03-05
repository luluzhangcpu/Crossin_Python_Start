
import requests

def guess():
    num0 = requests.get('https://python666.cn/cls/number/guess/')  # 随机本轮答案
    num = int(num0.text)
    times = 0
    while True:
        times += 1  # 猜的次数累加
        try:
            answer = int(input('猜一个 1～100 间的整数：'))
            if answer < num:
                print('猜小了，再试试')
            elif answer > num:
                print('猜大了，再试试')
            else:
                print('猜对了，你一共猜了%i轮' % (times))
                break  # 猜中后挑出循环
        except:
            print('输入有误，请重新输入')
    return times

def jilu(a ,c):
    b = [0 ,0 ,0 ,0]
    b[0 ] =a[0]
    b[1 ] =str(int(a[1] ) +1)
    if c > int(a[2]) and a[2] != '0':
        b[2] = a[2]
    else:
        b[2] = str(c)
    b[3] = str((int(a[1] ) *float(a[3]) + c ) /(int(a[1] ) +1))
    print(b[0] + '，你已经玩了%i次，最少%i轮猜出答案，平均%.2f轮猜出答案' % (int(b[1]) ,int(b[2]) ,float(b[3])))
    return b

try:
    with open ('/Users/apple/Desktop/Guess_number.txt') as f:
        record = f.readlines()
except:
    record = []


record2 = []
for i in record:
    j = i.split()
    record2.append(j)

name = input('请输入你的名字：')
line = [name ,'0' ,'0' ,'0']

for i in record2:
    if i[0] == name:
        line = i
        break

print(line[0] + '，你已经玩了%i次，最少%i轮猜出答案，平均%.2f轮猜出答案，开始游戏！' % (int(line[1]) ,int(line[2]) ,float(line[3])))

while True:
    line = jilu(line ,guess())
    a = input('是否继续游戏？（输入y继续，其他退出）')
    if a != 'y':
        break
print('游戏结束，欢迎下次再来！')

j = 0
for i in record2:
    if i[0] == line[0]:
        i = line
        break
    j += 1

try:
    record2[j] = line
except:
    record2.append(line)

with open('/Users/apple/Desktop/Guess_number.txt','w') as f:
    for i in record2:
        f.write(' '.join(i) + '\n')
