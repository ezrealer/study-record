# 让维护更简单---ItemLoader
[TOC]
###  i.引入ItmeLoader
```Python
from scrapy.loader import ItemLoader
```

### ii.通过ItemLoader加载item
*使用方法：*
```Python
item_loader = ItemLoader(item='你在爬虫文件中定义的item容器的名字',response = response)

1 item_loader.add_css('items.py中定义的字段', 'Css选择语法')
2 item_loader.add_xpath('items.py中定义的字段', 'Xpath选择语法')
3 item_loader.add_value('items.py中定义的字段', 具体的值)

#解析上面的规则
article_item = item_loader.load_item()
```

*具体代码：*
```python
#通过ItemLoader加载item
		item_loader = ItemLoader(item=JobBoleItem(),response = response)
		item_loader.add_css('title', '.entry-header h1::text')
		item_loader.add_value('url', response.url)
		item_loader.add_value('url_object_id', get_md5(response.url))
		item_loader.add_css('create_date', 'p.entry-meta-hide-on-mobile::text')
		item_loader.add_value('front_image_url', [response.url])
		item_loader.add_css('praise_num', '.vote-post-up h10::text')
		item_loader.add_css('comment_num', 'a[href="#article-comment"] span::text')
		item_loader.add_css('fav_num', '.bookmark-btn::text')
		item_loader.add_css('tags', 'p.entry-meta-hide-on-mobile a::text')
		item_loader.add_css('content', 'div.entry')

		article_item = item_loader.load_item() #调用规则并且进行解析
```
### iii.定制自己的item_loader
在`ii`中，已经使用item——Loader传递数据，现在，需要定义一些函数对数据进行处理，打开`items.py`文件：
*使用方法*
```python
from scrapy.loader.processors import MapCompose #包的作用：对传入的值调用函数

title = scrapy.Field(
		#对传入的值进行预处理
        input_processor = MapCompose(函数1，函数2，...，函数n)
        )
```
##### 可以在`items.py`中定义函数来处理需要处理的数据
```python
#定义处理时间函数：
#时间格式转换
def date_convert(value):
    try: 
        create_date = datetime.datetime.strptime(value, "%Y%m%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date
    
#引入函数
create_date = scrapy.Field(
        input_processor = MapCompose(date_convert)
        )
```
##### 对数组进行处理
###### 单个处理
```Python
from scrapy.loader.processors import TakeFirst
create_date = scrapy.Field(
        input_processor = MapCompose(date_convert)
        output_processor=TakeFisrt()
        )
```

###### 批量处理
自定义一个item字段：
```python
from scrapy.loader import ItemLoader
class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
```
然后在爬虫文件中引入刚刚写的类
```Python
from Bolespider.items import JobBoleItem, ArticleItemLoader
然后找到：
item_loader = ItemLoader(item=JobBoleItem(),response = response)
修改为：
item_loader = ArticleItemLoader(item=JobBoleItem(),response = response)
```
### iiii.处理点赞、评论、收藏数量等
##### 定义处理函数
打开`items.py`文件
```python
import re
#处理收藏、点赞、评论的数量
def get_nums(value):
    match_re = re.match('.*?(\d+).*', value)
    if match_re:
        num = int(match_re.group(1))
    else:
        num = 0
```
##### 需要的字段调用函数
```python
 praise_num = scrapy.Field(
        input_processor = MapCompose(get_nums)
        )
    comment_num = scrapy.Field(
        input_processor = MapCompose(get_nums)
        )
    fav_num = scrapy.Field(
        input_processor = MapCompose(get_nums)
        )
```

### V.`tags`字段转换
打开`items.py`文件
```Python
from scrapy.loader.processors import MapCompose, TakeFirst, Join #包的作用：对传入的值调用函数
定义函数：
#去掉tag中不要的字段的函数
def remove_comment_tags(value):
    if "评论" in value:
        return " "
    else:
        return value
引用刚刚写的函数：
tags = scrapy.Field(
        input_processor = MapCompose(remove_comment_tags)
        output_processor = Join(',')
        )
```

### VI.图片链接处理
```python
处理图片链接，把str还原成list
def return_value(value):
    return value
    
引用函数：
 front_image_url = scrapy.Field(
        output_processor = MapCompose(return_value)
        )
```


