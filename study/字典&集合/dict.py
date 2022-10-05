"""
											创建字典的两种方式：
"""
# 方式一：
p1 = {'name': '李白', 'age': 43}

print(p1)				# {'name': '李白', 'age': 43}
print(type(p1)) # <class 'dict'>


# 方式二：
p2 = dict(name = '杜甫', age = 57)

print(p2)				# {'name': '杜甫', 'age': 57}
print(type(p2)) # <class 'dict'>


# 查
print(p1['name'])  		# 李白
# print(p1['sex'])  	# 报错：KeyError: 'sex'

print(p2.get('name')) # 杜甫
print(p2.get('sex')) # 不报错：None


# 增
p1['sex'] = '男'
print(p1)			# {'name': '李白', 'age': 43, 'sex': '男'}


# 改
p1['age'] = 20
print(p1)			# {'name': '李白', 'age': 20, 'sex': '男'}


# 删
del p1['sex']
print(p1)			# {'name': '李白', 'age': 20}

p1.clear() # 清空字典元素
print(p1)     # {}



print('=========================================')

# 获取所有key
keys = p2.keys()

# print(keys[0])  # 报错：'dict_keys' object is not subscriptable
print(keys) 		  # dict_keys(['name', 'age'])
# 将所有的key组成的试图转成列表
print(list(keys)) # ['name', 'age']


# 获取所有value
values = p2.values()
# print(values[0])  # 报错：'dict_values' object is not subscriptable
print(values)    		# dict_values(['杜甫', 57])
# 将所有的value组成的试图转成列表
print(list(values)) # ['杜甫', 57]


# 获取所有的key-value对
items = p2.items()
# print(items[0]) 	# 报错：'dict_items' object is not subscriptable
print(items)  	 		# dict_items([('name', '杜甫'), ('age', 57)])
# 将所有的key-value组成的试图转成列表
print(list(items))	# [('name', '杜甫'), ('age', 57)]

print(list(items)[0]) 		# ('name', '杜甫')
print(list(items)[0][0])	# name



# 字典元素的遍历
print('-----------------------字典元素的遍历----------------')
for p in p2:
	print(p, p2[p], p2.get(p))

"""
name 杜甫 杜甫
age 57 57
"""



# 字典推导式  && zip
list = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]

d = {item:price for item, price in zip(list, prices)}

print(d)  # {'Fruits': 96, 'Books': 78, 'Others': 85}
