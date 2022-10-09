"""
	二分法查找算法：
		要求：数据必须有序排序
		核心思想：掐头结尾取中间
		每次查找都可以过滤一半的数据
"""
#    left            mid          right
lst = [12, 16, 22, 26, 34, 36, 42, 50]
#       0   1   2  3    4   5   6   7

print(lst)
n = int(input("请输入要查找的数字："))

left = 0
right = len(lst) - 1

while left <= right:
	mid = (left + right) // 2

	if n > lst[mid]:
		left = mid + 1

	elif n < lst[mid]:
		right = mid - 1
	else:
		print("我找到这个数了，她在%s位置" % mid)

		break

else:
	print("对不起，没有找到这个数！")