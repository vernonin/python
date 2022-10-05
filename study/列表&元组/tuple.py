"""
											创建元组的两种方式：
"""
# 方式一：
t0 = ('张无忌', '赵敏', 99)

# 元组中只包含一个元素时，必须带逗号。如果不带逗号会将左右括号默认视为运算符。
t1 = ('李白',) # <==> t1 ('李白', )

t2 = '三国演义', '西游记', '红楼梦', '水浒传'		# 省略了小括号

print(t0)					# ('张无忌', '赵敏', 99)
print(type(t0)) 	# <class 'tuple'>

print(t1)					# ('李白', )
print(type(t1))		# <class 'tuple'>

print(t2)					# ('三国演义', '西游记', '红楼梦', '水浒传')
print(type(t2))		# <class 'tuple'>



print('=============================================')

# 方式二：
tt = tuple(('java', 'python', 'go'))
print(tt)					# ('java', 'python', 'go')
print(type(tt))   # <class 'tuple'>



# 查
print(t0[0]) 		# 张无忌
print(t0[2])  	# 99
print(t0[-2]) 	# 赵敏
print(t2[1:3]) 	# ('西游记', '红楼梦')


# 改：报错
# t0[0] = '李白' 	 # 'tuple' object does not support item assignment


# 删：不能只删除元组中的某个元素，如果要删除，那么就使用del删除整个元组。
del tt
# print(tt) #  name 'tt' is not defined



# 遍历元组
print('-------------------遍历元组-------------------')
for t in t2:
	print(t, type(t))

"""
	三国演义 <class 'str'>
	西游记 <class 'str'>
	红楼梦 <class 'str'>
	水浒传 <class 'str'>
"""


# 使用推导式生成元组
numbers = (v for v in range(10))   # #返回一个迭代的对象

print(numbers)  	# <generator object <genexpr> at 0x00000122E7C56820>
# print(numbers[0]) # 报错：'generator' object is not subscriptable

for n in numbers:
	print(n)

"""
0
1
2
3
4
5
6
7
8
9
"""