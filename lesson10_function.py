
# task1
def func(x):
    print(x)
    return x+1

x = 2
print(func(x)) # 先输出2；再另起一行，输出 3

# task2
def func2(param):
    return param * 2

p = func2(20)
print(p) # 输出 40

# task3
def combine(l1,l2):
    for i in l1:
        if i not in l2:
            l2.append(i)
    l2.sort(reverse = False)
    return l2
print(combine([1,5,3],[2,6,7,4]))
