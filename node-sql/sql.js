var mysql = require('mysql')

//建立连接
var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	password: '69615345',
	database: 'test',
	port: '3306'
});

//创建连接
connection.connect(function (err) {
	if (err){
		console.log('[query]-:'+ err);
		return;
	}

	console.log('[connection connect] succeed!');
});

//插入数据
// var useradd = 'insert into user (uname, pwd) values(?,?)'
// var param = ['pzx', '154dfd'];
// connection.query(useradd, param, function (err, res) {
// 	if (err) {
// 		console.log('insert.err:' + err.message);
// 		return;
// 	}
// 	console.log('insrt succeed1');
// }) ;

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