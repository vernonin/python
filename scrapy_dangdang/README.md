
## 项目组成

```js

|-- scrapy_dangdang
|  |-- __pycache__
|  |-- spiders
|  |   |-- __init__.py
|  |   |-- 自定义的爬虫文件.py
|  |-- __init__.py
|  |-- items.py             // 定义数据结构的地方，是一个继承自scrapy.Item的类
|  |-- middlewares.py		    // 中间件  代理
|  |-- pipelines.py         // 管道文件，里面有一个类，用于处理下载数据的后续处理
|  |-- settings.py          // 配置文件， 比如：是否遵循robots协议， User--Agent定义 等
|-- scrapy.cfg


```