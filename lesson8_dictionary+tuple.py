# coding = utf-8

# task1
data = {'one':1,'two':2,'three':3}
data['two'] = 4
print(data)

# task2
str1 = 'Beautiful is better than ugly Explicit is\
 better than implicit Simple is better than complex Complex is \
better than complicated Flat is better than nested Sparse is better than dense'
dict1 = {}
for i in str1.split():
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
for i,k in dict1.items():
    print('%s : %d' % (i,k))
