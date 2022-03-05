with open('/Users/apple/Desktop/report.txt') as f:
    report = f.readlines()

scores = []
for i in report:
    data = i.split()
    scores.append(data)

scores[0].insert(0,'名次')
scores[0].extend(['总分','平均分'])

# 计算每个人总分、平均分(保留1位小数)，并添加至每个人的最后
for i in scores[1:]:
    sum = 0
    avg = 0
    for score in i[1:]:
        sum += int(score)
    avg = round(sum/len(i[1:]),1)
    i.extend([str(sum),str(avg)])

# 将结果按每个人的综合均分从高到低排序
result = sorted(scores,key=lambda x:x[len(scores[1])-1],reverse=True)

# 添加均分
sub_scores = []
num = len(result[1])
for j in range(1,num):
    sub_sums = 0
    sub_ave = 0
    if j < (num-1):
        for k in result[1:]:
            sub_sums += int(k[j])
        sub_ave = int(sub_sums/len(result[1:]))
        sub_scores.append(str(sub_ave))
    else:
        for k in result[1:]:
            sub_sums += float(k[j])
        sub_ave = round(sub_sums/len(result[1:]),1)
        sub_scores.append(str(sub_ave))

# 最前面插入'平均'字符串
sub_scores.insert(0,'平均')

# 将计算好的总均分，添入列表第2个位置
result.insert(1,sub_scores)

# 将名次对应，小于60分项替换成'不及格'
num2 = 0
for m in result[1:]:
    m.insert(0,num2)
    for n in m[2:len(m)-2]:
        if int(n)< 60:
            m[m.index(n)] = '不及格'
    num2 += 1

# 输出 result
with open('/Users/apple/Desktop/result.txt','w') as f:
    for result_list in result:
        for word in result_list:
            f.writelines(str(word) + ' ')
        f.writelines('\n')