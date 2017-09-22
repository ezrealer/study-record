# Node.js中exports与module.exports的区别
你肯定对Node.js模块中用来创建函数的exports对象很熟悉（假设一个名为rocker.js的文件）：
```javascript
exports.name = function() {
    console.log('My name is Ezreal');
};
```
然后你在另一个文件中调用：
```javascript
var rocker = require('./rocker.js');
rocker.name(); // 调用'My name is Ezreal'
```
但是module.exports到底是个什么玩意儿? 它合法吗？
令人吃惊的是 ```module.exports``` 是真实存在的东西。```exports``` 只是 ```module.exports``` 的辅助方法。你的模块最终返回 ```module.exports``` 给调用者，而不是 ```exports```。```exports``` 所做的事情是收集属性，如果```module.exports``` 当前没有任何属性的话，```exports```会把这些属性赋予```module.exports```。如果```module.exports```已经存在一些属性的话，那么exports中所用的东西都会被忽略。

把下面的内容放到rocker.js:
```javascript
module.exports = 'ROCK IT!';
exports.name = function() {
    console.log('My name is Ezreal');
};
```
然后把下面的内容放到另一个文件中，执行它：
```javascript
var rocker = require('./rocker.js');
rocker.name(); 
```
rocker模块完全忽略了`exports.name`，然后返回了一个字符串`’ROCK IT!’`。通过上面的例子，你可能认识到你的模块不一定非得是模块实例（`module instances`）。你的模块可以是任何合法的JavaScript对象 - boolean，number，date，JSON， string，function，array和其他。你的模块可以是任何你赋予`module.exports`的值。如果你没有明确的给`module.exports`设置任何值，那么`exports中的`属性会被赋给`module.exports中`，然后并返回它。
在下面的情况下，你的模块是一个类：
```javascript
module.exports = function(name, age) {
    this.name = name;
    this.age = age;
    this.about = function() {
        console.log(this.name +' is '+ this.age +' years old');
    };
};
```
然后你应该这样使用它：
```javascript
var Rocker = require('./rocker.js');
var r = new Rocker('Ozzy', 62);
r.about();
```
在下面的情况下，你的模块是一个数组：
```javascript
module.exports = ['Lemmy Kilmister', 'Ozzy Osbourne', 'Ronnie James Dio', 'Steven Tyler', 'Mick Jagger'];
```
然后你应该这样使用它：
```javascript
var rocker = require('./rocker.js');
console.log('Rockin in heaven: ' + rocker[2]); 
```
现在你应该找到要点了.如果你想要你的模块成为一个特别的对象类型，那么使用`module.exports`；如果你希望你的模块成为一个传统的模块实例（`module instance`），使用`exports`。

把属性赋予`module.exports`的结果与把属性赋予给`exports`是一样的。看下面这个例子：
```javascript
module.exports.name = function() {
    console.log('My name is Ezreal');
};
```
下面这个做的是一样的事情：
```javascript
exports.name = function() {
    console.log('My name is Ezreal');
};
```
但是请注意，它们并不是一样的东西。就像我之前说的`module.exports`是真实存在的东西，`exports`只是它的辅助方法。话虽如此，`exports`还是推荐的对象，除非你想把你模块 的对象类型从传统的模块实例（`module instance`）修改为其他的。