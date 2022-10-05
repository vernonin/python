"""
											创建集合的两种方式：
"""
# 方式一：
s1 = {2, 3, 4, 5, 5, 7, 7} # 集合中的元素不允许重复
print(s1)  	# {2, 3, 4, 5, 7}


# 方式二：
s2 = set(range(6))
print(s2)				# {0, 1, 2, 3, 4, 5}
print(type(s2))	# <class 'set'>

s3 = set([1,3, 5, 5, 5, 7, 7, 9])
print(s3)				# {1, 3, 5, 7, 9}

s4 = set((2, 4, 4, 4, 6, 6, 8))
print(s4)				# {8, 2, 4, 6} 集合中的元素是无序的

s5 = set('python')
print(s5)				# {'n', 'o', 'y', 'p', 't', 'h'}

s6 = set({'a', 'b', 'c', 'c'})
print(s6)				# {'b', 'c', 'a'}


# 定义空集合
ss = {}  		# 字典类型(dict)  ---> 错误
ss = set()  # 正确



print('=========================================')
# 增
s2.add(6)
s2.add('hello')
print(s2) 	# {0, 1, 2, 3, 4, 5, 6, 'hello'}

s2.update({10, 20, 30})
print(s2)		# {0, 1, 2, 3, 4, 5, 6, 10, 'hello', 20, 30}

s2.update((100, 200))
print(s2)		# {0, 1, 2, 3, 4, 5, 6, 100, 200, 10, 'hello', 20, 30}


# 删
s2.remove(200)
print(s2)		# {0, 1, 2, 3, 4, 5, 6, 100, 10, 20, 'hello', 30}
# s2.remove(500)  # 报错

s2.discard(100)
print(s2) 	# {0, 1, 2, 3, 4, 5, 6, 10, 'hello', 20, 30}
# s2.discard(500)	# 不报错

s2.pop()    # 删除一个任意元素
print(s2)

s2.clear()	# 清空集合
print(s2)   # set()

print("==============================================")

# 两个集合是否相等
s = {10, 20, 30, 40}
s1 = {30, 10, 40, 20}
print(s == s1) # True
print(s != s1) # False

# 一个集合是否另一个集合的子集
s3 = {10, 20, 30, 40, 50}
s4 = {10, 30}
s5 = {40, 80}
print(s4.issubset(s3)) # True
print(s5.issubset(s3)) # False

# 一个集合是否是另一个集合的超集
print(s3.issuperset(s4)) # True
print(s3.issuperset(s5)) # False

# 两个集合是否有交集
print(s3.isdisjoint(s4)) # False 有集合为 False
print(s3.isdisjoint(s5)) # False 有集合为 False
print(s4.isdisjoint(s5)) # True 没有交集为 True



print('---------------------------------------------')
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

# 交集
print(s1.intersection(s2))
print(s1 & s2) # intersection() 与 & 是等价的，交集操作

# 并集
print(s1.union(s2))
print(s1 | s2) # union() 与 | 是等价的，并集操作

# 差集
print(s1.difference(s2)) # {10, 20}
print(s2.difference(s1)) # {50, 60}
print(s1 - s2) # difference() 与 - 是等价的，差集操作

# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2) # symmetric_difference() 与 ^ 是等价的，对称差集操作



# 集合推导式
numbers = {i * i for i in range(6)}
print(numbers)  # {0, 1, 4, 9, 16, 25}
