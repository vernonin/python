"""
											创建列表的两种方式：
"""
# 方式一、
from asyncio import futures


lst1 = ['a', 'b', 0, 1]

# 方式二、
lst2 = list(['a', 'b', 0, 1])

print(lst1)  # ['a', 'b', 0, 1]
print(lst2)  # ['a', 'b', 0, 1]

print(lst1 == lst2) # True




"""
											列表的增删改查
"""
# 一、======================查======================

my_dream = ['healthy', 'happy', 'money', 'woman', 'healthy']

print(my_dream[0])   # healthy
print(my_dream[-1])  # healthy
print(my_dream.index('money'))  # 2

# 在指定区间查找
# print(my_dream.index('healthy', 1, 3)) # ValueError: 'healthy' is not in list
print(my_dream.index('healthy', 1, 5))   # 4




# 二、======================删======================

car = ['奔驰', '宝马', '奥迪', '三菱']
# 删除列表末尾的元素
car.pop()
print(car)    # ['奔驰', '宝马', '奥迪']

# 删除指定位置的元素
car.pop(1)
print(car)    # ['奔驰', '奥迪']




# 三、======================改======================

language = ['Java', 'C', 'C++', 'Python', 'Go']

language[3] = 'JavaScript'
print(language)   # ['Java', 'C', 'C++', 'JavaScript', 'Go']

language[-1] = 'TypeScript'
print(language)   # ['Java', 'C', 'C++', 'JavaScript', 'TypeScript']

language[0:3] = ['Html', 'CSS']
print(language)   # ['Html', 'CSS', 'JavaScript', 'TypeScript']




# 四、======================增======================

phone = ['iphoen']

# 在列表末尾添加一个
phone.append('huawei')
print(phone)   # ['iphoen', 'huawei']

# 在列表末尾添加多个
phone.extend(['SAMSUNG', 'millet'])
print(phone)   # ['iphoen', 'huawei', 'SAMSUNG', 'millet']

# 在任意位置添加一个
phone.insert(1, 'vivo')
print(phone)   # ['iphoen', 'vivo', 'huawei', 'SAMSUNG', 'millet']

# 在任意位置添加多个
test_list = [1, 'hi', False]
phone[2:] = test_list
print(phone)  # ['iphoen', 'vivo', 1, 'hi', False]







"""
											列表的其他操作
"""

fruits = ['苹果', '西瓜', '香蕉', '菠萝', '橙子']

# 获取列表的长度
print(len(fruits))   # 5

# 遍历列表 方式一、
for item in fruits:
	print(item)

# 遍历列表 方式二、
for item in range(len(fruits)):
	print(f'{item}：{fruits[item]}')


# 反转列表中元素
fruits.reverse()
print(fruits)   # ['橙子', '菠萝', '香蕉', '西瓜', '苹果']