# ES数据
## 1 数据吞吐
无论程序怎么写,意图是一样的:组织数据为我们的目标所服务。但数据并不只是由随机比特和字节组成,我们在数据节点间建立关联来表示现实世界中的实体或者“某些东西”。属于同一个人的名字和Email地址会有更多的意义。
在现实世界中,并不是所有相同类型的实体看起来都是一样的。
一个人可能有一个家庭电话号码,另一个人可能只有一个手机号码,有些人可能两者都有。一个人可能有三个Email地址,其他人可能没有。西班牙人可能有两个姓氏,但是英国人(英语系国家的人)可能只有一个。
面向对象编程语言之所以受欢迎,一个原因是对象帮助我们表示和处理现实生活中包含潜在复杂结构的实体。到目前为止这非常好。当我们想存储这些实体时问题便来了。传统上,我们以行和列的形式把数据存储在关系型数据库中,相当于使用电子表格。这种固定的存储方式导致对象的灵活性不复存在了。但是如何能以对象的形式存储对象呢?相对于围绕表格去为我们的程序去建模,我们可以专注于使用数据,把对象本来的灵活性找回来。
对象(object)是特定语言(language-specific)和内存式(in-memory)的数据结构。为了在网络间发送,或者存储它,我们需要一些标准的格式来表示它。JSON	(JavaScript	Object	Notation)是一种可读的以文本来表示对象的方式。它已经成为NoSQL世界中数据交换的一种事实标准。当对象被序列化为JSON,它就成为JSON文档(JSON	document)了。
Elasticsearch是一个分布式的文档(document)存储引擎。它实时的可以存储并检索复杂的数据结构——序列化的JSON文档。换言说,一旦文档被存储在Elasticsearch中,它在集群的任一节点上就可以被检索。
当然,我们不仅需要存储数据,还要快速的批量查询。虽然已经有很多NoSQL的解决方案允许我们以文档的形式存储对象,
但它们依旧需要考虑如何查询我们的数据,以及哪些字段需要被索引以便让数据检索更加快速。
在Elasticsearch中,每一个字段的数据都是默认被索引的。也就是说,每个字段专门有一个反向索引用于快速检索。而且,与其它数据库不同,它可以在同一个查询中利用所有的这些反向索引,以惊人的速度返回结果。
在这一章我们将探讨如何使用API来创建、检索、更新和删除文档。目前,我们并不关心数据如何在文档中以及如何查询他们。所有我们关心的是文档如何安全Elasticsearch中存储,以及如何让它们返回。

## 2 文档

### 2.1 什么是文档
程序中大多的实体或对象能够被序列化为包含键值对的JSON对象,键(key)是字段(field)或属性(property)的名字,值
(value)可以是字符串、数字、波尔类型、另一个对象、值数组或者其他特殊类型,比如表示日期的字符串或者表示地理位置的对象。
```Json
{
				"name":									"John	Smith",
				"age":										42,
				"confirmed":				true,
				"join_date":				"2014-06-01",
				"home":	{
								"lat":						51.5,
								"lon":						0.1
				},
				"accounts":	[
								{
												"type":	"facebook",
												"id":			"johnsmith"
								},
								{
												"type":	"twitter",
												"id":			"johnsmith"
								}
				]
}
```
通常,我们使用可互换的对象(object)和文档(document)。然而,还是有区别的。对象(Object)仅是一个JSON对象——类似于哈希、hashmap、字典或者关联数组。对象(Object)则可以包含其他对象(Object)。
在Elasticsearch中,文档(document)这个术语有着特殊含义。它指的是拥有唯一ID的最顶层或者根对象(root	object)序列化成的JSON。

### 2.2 文档元数据
一个文档不只有数据。它还包含了元数据(metadata)——关于文档的信息。三个必须的元数据节点是:

|节点|说明|
|--------|--------|
|_index|文档存储的地方|
|_type|文档代表的对象的类|
|_id|文档的唯一标识|

### 2.3 其它元数据
还有一些其它的元数据,我们将在《映射》章节探讨。使用上面提到的元素,我们已经可以在Elasticsearch中存储文档并通过ID检索——换言说,把Elasticsearch做为文档存储器使用了。

## 3 索引
### 3.1 索引一个文档
文档通过`index`API被索引——使数据可以被存储和搜索。但是首先我们需要决定文档所在。正如我们讨论的,文档通过其`_index、_type、_id`唯一确定。们可以自己提供一个_id,或者也使用`index API`为我们生成一个。
#### 3.1.1 使用自己的ID
如果你的文档有自然的标识符(例如`user_account`字段或者其他值表示文档),你就可以提供自己的`_id`,使用这种形式的`index	API:`
```json
PUT	/{index}/{type}/{id}
{
		"field":	"value",
		...
}
```
例如我们的索引叫做 	“website”	 ,类型叫做 	“blog”	 ,我们选择的ID是 	“123”	 ,那么这个索引请求就像这样:
```
PUT	/website/blog/123
{
		"title":	"My	first blog entry",
		"text":		"Just trying this out...",
		"date":		"2014/01/01"
}
```
Elasticsearch的响应:
```json
{
			"_index":	"website",
			"_type":	"blog",
			"_id":		"123",
			"_version":	1,
			"created":	true
}
```
响应指出请求的索引已经被成功创建,这个索引中包含 _index	、_type和_id元数据,以及一个新元素:_version。

#### 3.1.2 自增ID
如果我们的数据没有自然ID,我们可以让Elasticsearch自动为我们生成。请求结构发生了变化: PUT方法—— “在这个URL中存储文档”变成了POST方法—— "在这个文档下存储文档" 。(译者注:原来是把文档存储到某个ID对应的空间,现在是把这个文档添加到某个 _type下)。
URL现在只包含 _index和 _type两个字段:
```json
POST /website/blog/
{
		"title": "My second blog	entry",
		"text":	"Still trying this	out...",
		"date":	"2014/01/01"
}
```
响应内容与刚才类似,只有_id	字段变成了自动生成的值:
```json
{
			"_index": "website",
			"_type": "blog",
			"_id":	"wM0OSFhDQXGZAWDf0-drSA",
			"_version":	1,
			"created":	true
}
```
自动生成的ID有22个字符长,URL-safe,	Base64-encoded	string	universally	unique	identifiers,	或者叫	UUIDs。
