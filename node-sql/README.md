# NodeJs连接MySQL

## 连接准备

```
$ mkdir node-sql && cd node-sql
$ npm install mysql
$ vim sql.js
```
<p style="color:red"><em>上面的命令执行完毕后，你创建了一个文件夹，安装了NodeJS的MySQL模块，并且创建了一个名为sql.js的文件</em></p>
<p style='color:aqua'>现在，在你的编辑器中打开sql.js:</p>

```javascript
var mysql = require('mysql') //请求MySQL模块
//建立连接
var connection = mysql.createConnection({
	host: 'localhost',//服务器地址
    user: 'root', //数据库用户名
    password: '***'//数据库密码
    database: 'test' //数据库名称
    port: '3306' //数据库端口
});
```
<p style="color:aqua">现在，连接已经建立了，接下来，使用这个连接:</p>

```javascript
connection.connect(function (err) {
	if (err){
		console.log('[query]-:'+ err);
		return;
	}

	console.log('[connection connect] succeed!');
});
```
<p style="color:aqua">创建的连接被一个名为connect的函数调用，该函数返回两个值：连接成功返回res，连接失败返回err,成功后可以对数据进行操作</p>

## 具体操作

```JavaScript
//插入数据
var useradd = 'insert into user (uname, pwd) values(?,?)'
var param = ['pzx', '154dfd'];
connection.query(useradd, param, function (err, res) {
	if (err) {
		console.log('insert.err:' + err.message);
		return;
	}
	console.log('insrt succeed1');
}) ;

//查询
connection.query('SELECT * FROM user where uid = 6', function(err, res){
	if (err) {
		console.log('[query]:'+err);
		return;
	}
	for (var i = 0; i < res.length; i++) {
		console.log('结果:',res[i].uname);
	}
});

//关闭连接
connection.end(function (err) {
	if (err) {
		console.log(err.toString());
		return;}
	console.log('[connection end] succeed!');	
});
```
## 结语
<p style="color:aqua">V1.0版本，未建立连接池，持续更新...</p>

![  ](0031.jpg)

