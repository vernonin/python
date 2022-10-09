"""
	冒泡排序(Bubble Sort):
		它重复地走访过要排序的元素列，依次比较两个相邻的元素
		如果顺序(如从大到小、首字母从Z到A)错误就把他们交换过来。
		走访元素的工作是重复地进行，直到没有相邻元素需要交换，也就是说该元素列已经排序完成。
"""

list = [23, 18, 42, 124, 32, 74, 140]
leng = len(list)

for i in range(0, leng):
	for j in range(i + 1, leng):
		if (list[i] > list[i + 1]):
			list[i], list[j] = list[j], list[i]


print(list)