# coding = utf-8

# task1
lst = [1,2,3]
print(lst[0])
lst[1] = 4
lst.append(5)
print(lst)

# task2
lst = [365,'everyday',0.618,True,2,5]
lst2 = lst[1:-1]
print(lst2)

# task3
word = 'I am Mr Crossin of Python'
lst = word.split()
print(lst)
word = ','.join(lst)
print(word)