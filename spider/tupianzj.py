"""
	目标网站: https://www.tupianzj.com/meinv/xinggan/list_176_1.html
	任务：爬取图片之家中所有的性感美女土
"""

import time
import requests
from bs4 import BeautifulSoup

base_url = "https://www.tupianzj.com"

header = { # 请求头
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

# 请求每页的函数
def get_page(url):
	res = requests.get(url, headers=header)
	res.encoding = "gb2312"

	page_html = BeautifulSoup(res.text)

	li_list_html = page_html.find("ul", class_="list_con_box_ul").find_all("li")

	for li in li_list_html:
		detail_url = li.find("a")["href"]
		detail_url = base_url + detail_url

		title = li.find("a")["title"]

		get_detail_page(detail_url, title)

		time.sleep(2)



# 请求详情页函数
def get_detail_page(url, title):
	res = requests.get(url, headers=header)
	res.encoding = "gb2312"

	detail_page_html = BeautifulSoup(res.text)

	img_src = detail_page_html.find("div", class_="pic_tupian").find("img")["src"]
	
	if not img_src.startswith("https"):
		img_src = base_url + img_src

	download(img_src, title)


# 下载图片函数
def download(url, title):
	res = requests.get(url, headers=header)
	with open(f"images\{title}.jpg", "wb") as f:
		f.write(res.content)
		print(f"{title}下载完成！")



# 主函数
def main():
	# 爬去一页
	url = "https://www.tupianzj.com/meinv/xinggan/list_176_26.html"
	get_page(url)

	# 爬去多页
	# for i in range(1, 11):
	# 	url = "https://www.tupianzj.com/meinv/xinggan/list_176_" + i + ".html"
	# 	get_page(url)

	# 	time(1)


if __name__ == "__main__":
	main()
