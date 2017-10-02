# Scrapy基础知识
#### scrapy VS requests+beatifulsoup
1.requests和beatifulsoup都只是库；scrapy是框架，更加强大。
2.scrapy框架中可以加入requests和beatifulsoup
3.scrapy基于twisted，性能是最大的优势
4.scrapy方便拓展，提供了许多内置的功能
5.scrapy内置的css和xpath selector非常方便；beatifulsoup最大的缺点就是慢

#### 常见的网页服务
1.静态网页
事先生成好在服务器的文件，不可以客户端发生改变。
2.动态网页
有数据请求，客户请求后会发生改变。
3.webservice(restapi)

#### 爬虫的作用
1.搜索引擎---百度、Google、垂直领域搜索引擎
2.推荐引擎--今日头条
3.机器学习的数据样本
4.数据分析
...
...