# scrapy

Scrapy 是用 Python 实现的一个为了爬取网站数据、提取结构性数据而编写的应用框架。


## Scrapy架构图

![img](https://www.runoob.com/wp-content/uploads/2018/10/8c591d54457bb033812a2b0364011e9c_articlex.png)

## 开始
### 1.安装
```py
pip install Scrapy
```

### 2.创建项目
```py
scrapy startproject [项目名字]
```

目录结构
```py

|-- scrapy_project_name
|  |-- __pycache__
|  |-- spiders
|  |   |-- __init__.py
|  |   |-- [自定义的爬虫文件].py
|  |-- __init__.py
|  |-- items.py  		# 定义数据结构的地方，是一个继承自scrapy.Item的类
|  |-- middlewares.py	# 中间件  代理
|  |-- pipelines.py     # 管道文件，里面有一个类，用于处理下载数据的后续处理
|  |-- settings.py      # 配置文件， 比如：是否遵循robots协议， User--Agent定义 等
|-- scrapy.cfg
```

### 3.跳转到spiders文件夹下
```py
cd [项目名字]\[项目名字]\spider
```

### 4.创建爬虫文件
```py
scrapy genspider -t crawl [爬虫文件的名字] [爬虫文件的地址]
```

### 5. 运行
```
scrapy crawl [爬虫文件的名字]
```