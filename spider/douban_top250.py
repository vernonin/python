# -*-coding:utf-8-*-

from bs4 import BeautifulSoup						 # 网页解析，获取数据
import re                                # 正则表达式，进行文字匹配
import urllib.request, urllib.error      # 制定URL，获取网页数据
import xlwt															 # 进行Excel文件操作


def main():
	baseurl = "https://movie.douban.com/top250?start="
	
	print("------------------------")
	print("|                      |")
	print("|       开始下载...    |")
	print("|                      |")
	print("------------------------")

	dataList = getData(baseurl)

	savepath = ".\\豆瓣电影Top250.xls"

	saveData(dataList, savepath)


findLink = re.compile(r'<a href="(.*?)">')  # 创建电影连接正则表达式对象
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S) # 创建电影图片正则表达式对象
findTitle = re.compile(r'<span class="title">(.*)</span>')  # 创建电影名称正则表达式对象
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>') # 创建电影评分正则表达式对象
findJuge = re.compile(r'<span>(\d*)人评价</span>') # 创建电影评价人数正则表达式对象
findInq = re.compile(r'<span class="inq">(.*?)</span>')  # 创建电影概识正则表达式对象
findBd = re.compile(r'<p class="">(.*?)</p>', re.S) # 创建电影导演演员正则表达式对象

# 1.爬去网页
def getData(baseurl):
	dataList = []

	for i in range(0, 10):
		url = baseurl + str(i * 25)

		html = askURL(url)
		
		# 逐一解析
		soup = BeautifulSoup(html, "html.parser")

		# soup.find_all("div", class_="item"): 查找class为“item”的div
		for item in soup.find_all("div", class_="item"):
			data = []

			item = str(item)

			link = re.findall(findLink, item)[0]     # 电影详情链接
			data.append(link)

			imgSrc = re.findall(findImgSrc, item)[0] # 电影图片链接
			data.append(imgSrc)

			title = re.findall(findTitle, item)[0]   # 电影名称
			data.append(title)

			rating = re.findall(findRating, item)[0] # 电影评分
			data.append(rating)

			juge = re.findall(findJuge, item)[0]     # 电影评价人数
			data.append(juge)

			inq = re.findall(findInq, item)          # 电影概识
			if len(inq) != 0:
				inq = inq[0].replace("。", "")
				data.append(inq)
			else:
				data.append("")
				
			bd = re.findall(findBd, item)[0]         # 电影导演及主演
			bd = re.sub('<br/>', "", bd)
			bd = re.sub('\s', "", bd)
			data.append(bd)

			dataList.append(data)


	return dataList


# 得到制定一个URL的网页内容
def askURL(url):
	# 伪装浏览器访问
	head = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
	}

	request = urllib.request.Request(url, headers = head)
	html = ""

	try:
		response = urllib.request.urlopen(request)

		html = response.read().decode("utf-8")

		return html
	except urllib.error.URLError as err:
		if hasattr(err, "code"):
			print(err.code)

		if hasattr(err, "reason"):
			print(err.reason)

# 2.保存数据
def saveData(dataList, savepath):
	xl = xlwt.Workbook(encoding="utf-8")
	sheet = xl.add_sheet("豆瓣电影Top250")
	col = ("电影详情链接", "封面链接", "影片名称", "评分", "评价人数", "概识", "相关信息")

	for i in range(0, 7):
		sheet.write(0, i, col[i])   # 写入列名

	for i in range(0, 250):
		print("第%d条"%(i + 1))
		data = dataList[i]
		for f in range(0, 7):
			sheet.write(i + 1, f, data[f])  # 写入数据

	xl.save(savepath)

	print("------------------------")
	print("|                      |")
	print("|      下载完成！      |")
	print("|                      |")
	print("------------------------")
	

if __name__ == '__main__':
	main()