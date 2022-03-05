# coding = utf-8
# task1
name = 'Crossin'
age = 18
code = 'Python'
result = '%s is %d, he writes %s.' % (name,age,code)
print(result)

# task2
num1 = '3.3'
num2 = 2.5
num1 = float(num1)
print(num1 + num2)

# task3
print(bool(123)) # True
print(bool(0)) # False
print(bool('abc')) # True
print(bool('')) # False
print(bool([])) # False
print(bool({})) # False
print(bool([''])) # True
print(bool(None)) # False