# 前端基础知识

## Node.js服务端的语言

在编写前端代码时可以使用**VScode**代码编辑工具进行编写，下载地址：[https://code.visualstudio.com/](https://code.visualstudio.com/){target="_blank"}

### 下载Node.js

* 下载地址：[https://nodejs.org/zh-cn/download](https://nodejs.org/zh-cn/download){target="_blank"}
* 帮助文档：[https://nodejs.org/zh-cn/docs](https://nodejs.org/zh-cn/docs){target="_blank"}
* 关于Nodejs：[https://nodejs.org/zh-cn/about](https://nodejs.org/zh-cn/about){target="_blank"}
* 安装后检查是否安装成功cmd输入`node -v`
* Node.js是一门计算机语言，运行在系统中的V8（jvm）引擎中。文件后缀`js`运行命令：node

<!-- more -->

### Node.js是什么

* **node.js是一种服务端的语言**

* node.js一种javascript的运行环境，能够使得javascript脱离浏览器运行

* node.js是一个基于Chrome JavaScript运行时建立的平台

* node.js是基于Google的V8引擎

### JavaScript与node.js的区别

JavaScript：

* `ESMAScript`(语言基础，如：语法、数据类型结构以及一些内置对象)
* `DOM`(操作页面元素)
* `BOM`(操作浏览器的方法)

Node.js:

* `ESMAScript`(语言基础，如：语法、数据类型结构以及一些内置对象)
* `os`(操作系统)
* `file`(文件系统)
* `net`(网络系统)
* `database`(数据库)

### node.js的基本用法

输出hello-word:

* 创建hello-word.js文件

    ```js
    console.log("hello word!!!");//在控制台输出hello word!!!
    ```

    在终端输入`node helloword.js`

实现HTTP请求和响应

* 创建一个`httpserlvet.js`文件

```js
const http = require("http");     //require导入模块
http.createServer(function(request,response){ //1.创建一个httpservler服务
    response.writeHead(200,{'Content-type':'text/html'});//告诉浏览器用text-plain解析hello server这段数据
    response.end("<h1>hello server!!!<h1>");//浏览器输出内容
}).listen(8888);

console.log("你启动的服务是http://localhost:8888以启动成功");

//1.require导入模块
//2.创建一个httpservler服务
//3.监听端口8888
//4.启动运行服务node httpserlvet.js
//5.在浏览器访问http://localhost:8888
```

在终端输入`node httpserlvet.js`

实现MySQl数据库操作

* 创建一个`database.js`文件

```js
var mysql = require("mysql");     //导包
var connection = mysql.createConnection({  //创建一个mysql连接、配置数据库连接信息
    host:"localhost",
    user:"root",
    port:"3306",
    password:"123321",
    database:"junit"
});
connection.connect();       //开启连接
connection.query("select * from classes",function(error,result,fields){//创建SQL语句
    if(error)throw error;      //如果程序错误，抛出
    console.log("result=",result);    //查询成功
});
connection.end();        //关闭连接
//运行node db.js
```

在终端输入`node database.js`

## ES6新规范

### 什么是ES6

* JavaScipt是由：`ECMAScript`、`Dom`、`Bom`组成。
* ES5：ECMAScript的第五个版本
* ES6：ECMAScript的第六个版本，保证向下兼容的前提下，提供大量新特性
* ES6提供的基本的新特性有

### ES6的常见的新特性

let 和 const关键字、模板字符串、函数默认参数、箭头函数、对象初始化，对象解构、传播操作符、数组map和reduce方法使用

* let 和 const关键字

```js
let name = "zhangsan";  // let:定义变量
const PI = Math.PI;   // const:定义常量
for(var i=0;i<5;i++){  //使用ES5:var定义，变量穿透问题
    console.log(i);
};
var PI=Math.PI;    //使用ES5:var定义，变量更改问题
PI = 100;
```

* 模板字符串

```js
console.log('hello ' + name)//ES5方式
console.log(`hello ${name}`)//ES6方式，类似于Java中el表达式 `为键盘数字1左边的键英文输入`
```

* 函数默认参

```js
function add(a =100,b=100) {//设置函数默认参
    console.log(a,b);    
}
```

* 箭头函数(`=>`)

**规则**:

  1. `function`关键字用`=>`代替
  2. 当只有一个参数时可以省略
  3. 如果逻辑体只有`return`关键字可以省略
  4. 支持继承上下文的`this`关键字

```js
var sum = function(a){ //ES5
    return a+b;
};
var sum = a=> a+b;  //ES6:当只有一个参数时可以省略括号
        
var sum = function(a，b{ //ES5
    return a+b;
};      
var sum = (a,b)=> a+b; //ES6:多个参数时不可省略括号

var sum = function(a，b{ //ES5
    const s=a+b;                
    return s;
};      
var sum = (a,b)=>{   //ES6:当有逻辑体时不可以省略大括号
  const s=a+b;                
    return s;
}; 
```

* 对象初始化

```js
var info = {   //ES5
      title:"document",
      link:"文档",
      go:function(){
            console.log("es5-加油加油加油！！！");
        }
      };
console.log(info);
//因为对象key:value的形式存在,如果key和变量名字一致，可以只定义一次    
const title="document"; //ES6
const link="文档";
let info2 = {
      title,
      link,
      go(){
          console.log("es6-加油加油加油！！！");
        }
      };
console.log(info2);
```

* 对象解构

```js
const title="document";
const link="文档";
    let info2 = {
        title,
        link,
        go(){
            console.log("es6-加油加油加油！！！");
        }
    };
//ES5中，对象是key:value存在，获取对象属性和方法的两种方式. 、[]
    info2.link;
  info2.go();
    info2["link"];
    info2["go"]();
//ES6对象解构-快速获取属性和方法的方式
    var {title,link,go} = info2;
    console.log(title,link,go);
```

* 传播操作符

```js
/**
 * 对象传播操作符:在对象解构的过程中如果对象属性太多或者想把对象中属性全部解构出来就可以使用{a,b,...c} | {...c}其中...为传播操作符
  * */
var person = {
    name:"攀岩",
    addres:"跑步",
    link:"奋斗",
    phone:123456,
    go(){
            console.log("为了梦想加油加油加油！！！");
        }
    };
//使用传播操作符快速解构
var {name,addres,...person2} = person;
    console.log(name);
    console.log(addres);
    console.log(person2);
//可以简化为
var {...person3} = person;
    console.log(person3);
```

* 数组map

```js
var arr = [1,2,3,4,5,6,7];
let newarr = [];      //ES5方式循环遍历
    for(let i=0;i<arr.length;i++){
            newarr.push(arr[i]*2);
    }
    console.log(newarr);
var newarr2 = arr.map(function(ele){ //ES6方式遍历循环
    return ele * 2;      //map方式:自带循环并且会把处理的值回填对应的位置，自带循环、回填
});
var newarr3 = arr.map(ele=>ele * 2)  //箭头函数简写

//map方式处理对象的数据:自增+1、并添加属性、可以对json格式的数据进行改造
var users = [{age:10,name:"小学"},{age:15,name:"中学"},{age:20,name:"大学"}];
var newusers = users.map(function(ele){
      ele.age = ele.age + 1;    //map自增+1
      ele.check=true;     //map添加属性
      return ele;
      });
var newuser2 = users.map(ele=>{   //箭头函数简写
  le.age = ele.age + 1;
    ele.check=true;
    return ele;
});
```

* reduce方法使用

```js
var arr = [1,2,3,4,5,6,7];
var result =  arr.reduce(function(a,b){ //reduce()方法实现数组中数据相加
      return a+b;
});
var result2 =  arr.reduce((a,b)=>a+b); //箭头函数简写
```

* 概括

    `ES6`是`ES5`的拓展版，`let 可变`，`const不可变`。模板字符串拼接使用`${..}`。`=>`对函数的简写。对象初始化默认参数。对象统一解构。传播符`（...A）`。`map`-自带循环、回填，可更改添加属性。`reduce方法`对数组（对象）中的数进行依次相加。

* `Node.js`与`JavaScript`、`ES5`、`ES6`之间的关系

  1. `Node.js` 是 `JavaScript` 的服务器**运行环境**。
  2. `JavaScript`包括`ECMAScript`、`DOM`、`BOM` 。
  3. `ES6`在`ES5（ECMAScript）`的基础上添加了新规范。
  4. `Node.js` 对`ES6` 的支持度更高。

## Npm包管理器

### Npm包管理器是什么

* 由于nodejs是一种服务端的语言，可以对数据库浏览器等进行操作所有在nodejs要导入这些依赖，可以使用npm包管理器来导入依赖。
* npm是Nodejs平台的默认包管理工具，所以npm会随同NodeJS一起安装。可以根据配置package.json下载js库。类似于Java的maven。
* 官方网站：[https://www.npmjs.com/](https://www.npmjs.com/)

### 使用

```cmd
npm -v #在命令提示符输入
```

* 在当前项目下初始化Npm包管理器

```cmd
npm init # 方式1
#配置package.json文件信息
{
  "name": "npm",                      #工程名
  "version": "1.0.1",                 #项目版本
  "description": "我是一个node工程",   #描述
  "main": "index.js",                 #入口js
  "scripts": {                        #运行脚本
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "node"
  ],
  "author": "xxx",                    #开发者
  "license": "ISC"                    #授权协议
}
npm init -y # 方式2
# 直接生成 package.json 文件
```

* 切换淘宝镜像

```cmd
npm config set registry https://registry.npm.taobao.org #npm install 都会经过淘宝的镜像地址下载
npm config list  #查看npm配置信息，切换淘宝镜像后可以使用cnpm
```

* **npm install命令**

```cmd
cnpm install jquery
# 下载的模块会安装到：项目目录\node_modules，安装后会自动添加package-lock.json文件，这个文件帮助锁定安装包的版本
# 同时package.json 文件中，依赖包会被添加到dependencies节点下，类似maven中的 <dependencies>
cnpm install jquery@2.1.x #如果安装时想指定特定的版本
cnpm install -g webpack
#全局安装
#Node.js全局安装的npm包和工具的位置：用户目录\AppData\Roaming\npm\node_modules
#一些命令行工具常使用全局安装的方式
```

* **其他命令**

```cmd
cnpm update <包名>    #更新包（更新到最新版本）
cnpm update -g <包名>   #全局更新
cnpm uninstall <包名>   #卸载包
cnpm uninstall -g <包名>  #全局卸载
```

* **package-lock.json与package.json的区别**

    package.json记录当前项目所依赖模块的版本信息，更新模块时锁定模块的大版本号（版本号的第一位）。package-lock.json记录了node\_modules目录下所有模块的具体来源和版本号以及其他的信息。

## Babel转码器

### Babel转码器是什么

* ES6的某些高级语法在浏览器环境或者是Node.js环境中无法执行
* Babel是一个广泛使用的转码器，可以将ES6代码转为ES5代码，从而在现有环境执行

### 如何使用

* 安装Babel

```cmd
cnpm install -g babel -cli
babel --version #查看是否 安装成功
```

* 创建Babel文件夹

* 初始化项目（Npm包管理器）

```cmd
cnpm init -y
```

* 创建要解码的js

```js
let input = [1, 2, 3]
input = input.map(item => item + 1)
```

* 配置.babelrc

> Babel的配置文件是.babelrc，存放在项目的根目录下，该文件用来设置转码规则和插件，基本格式如下。

```js
//presets字段设定转码规则，将es2015规则加入 .babelrc：   
{
    "presets": ["es2015"],
    "plugins": []
}
```

* 安装解码器

```js
cnpm install --save-dev babel-preset-es2015
```

* 转码

```cmd
# npm install --save-dev csv-loader xml-loader
# 转码结果写入一个文件
mkdir dist1
# --out-file 或 -o 参数指定输出文件
babel src/example.js --out-file dist1/compiled.js
# 或者
babel src/example.js -o dist1/compiled.js
# 整个目录转码
mkdir dist2
# --out-dir 或 -d 参数指定输出目录
babel src --out-dir dist2
# 或者
babel src -d dist2
```

* 方式二自定义脚本转码

1、改写package.json

```json
{
    // ...
    "scripts": {
        // ...
        "build":  "babel src\\example.js -o dist\\compiled.js"
    },
}
```

2、转码

```cmd
mkdir dist
cnpm run build
```

## 模块化开发

### 什么是模块化开发

现在网页元素越来越丰富，前端代码JavaScript越来越庞大，越来越复杂。如果没有像Java那样包、类模块发的编程，因此针对JavaScript推出了模块化归还，让开发者只需要实现核心的业务逻辑。其他都可以加载别人已经写好的模块。

### CommonJS规范

**CommonJS使用 exports 和require 来导出、导入模块**:

* 创建common-js.js文件

```js
const sum = function(a,b){  //加
    return a + b
}
const subtract = function(a,b){ //减
    return a - b
}
const multiply = function(a,b){ //乘
    return a * b
}
const divide = function(a,b){ //除
    return a / b
}
module.exports = {    //使用module.exports导出该文件的成员
    sum,
    sub,
    mul,
    di
};
```

* 创建common-js-require.js文件

```js
const m = require("./common-js.js");//使用require()导入common-js.js模块化开发
console.log(m.sum(9,1));   //输出
```

* 运行程序

```cmd
node common-js-require.js
```

### ES6模块化规划

**ES6使用 export 和 import 来导出、导入模块。**

* 创建userExport.js文件

```js
export default{
    getList(){
        // 在真实业务开发中，异步获取数据
        console.log("获取数据列表");
    },
    save(){
        // 在真实业务开发中，异步获取数据
        console.log("保存数据");
    }
}
```

* 创建userImport.js文件

```js
import userApi from './userExport.js'
userApi.getList()
userApi.save()
```

> ES6在模块化开发中无法在Node.js中执行，需要使用Babel编辑成ES6后再执行

* 初始化项目

```cmd
cnpm init -y
```

* 配置.babelrc

```js
{
    "presets": ["es2015"],
    "plugins": []
}
```

* 安装转码器

```cmd
cnpm install --save-dev babel-preset-es2015

```

* 定义运行脚本，package.json中增加"build"

```js
{
    // ...
    "scripts": {
        "build": "babel src -d dist"
    }
}
```

* 执行命令转码

```cmd
cnpm run build
```

* 运行程序

```js
node dist/userExport.js
```

## Webpack前端打包编译工具工具

### Webpack什么是

webpack作用：可以将多个静态资源js、css等打包成一个js文件。

### 安装

* 全局安装

```cmd
npm install -g webpack webpack-cli
```

* 查看版本号

```js
webpack -v
```

### 打包.js

实现步骤：

1. 创建两个js文件
2. 创建文件入口main.js
3. 创建webpack配置文件
4. 运行webpack命令
5. 创建index.html页面测试

* 创建两个js

```js
exports.info = function(str){//导出
    console.log(str);   //控制台
    document.write(str);  //浏览器
}

```

```js
exports.add = (a,b) =>a+b;  //相加函数
```

* 创建入口文件main.js

```js
const util = require("./util");//导入util、common
const common = require("./common");
common.info("Helloword,"+util.add(100,100));
```

* 创建webpack配置文件`webpack.config.js`

```js
const path = require("path");  //导入path模块
module.exports = {      //定义JS打包的规则
    entry:"./src/main.js",
    output:{
        path:path.resolve(__dirname,"./dist"),
        filename:"bundle.js"
    }
}

```

> **entry:**读取当前项目目录下src文件夹中的main.js（入口文件）内容，分析资源依赖，把相关的js文件打包，**output:path**打包后的文件放入当前目录的dist文件夹下，**filename:**打包后的js文件名为bundle.js

* 配置项目的npm运行命令，修改package.json文件

```js
"scripts": {
    //...,
    "dev": "webpack --mode=development"
}
//或者cmd输入:webpack --mode=development表示执行后查看bundle.js 里面包含了上面两个js文件的内容并进行了代码压缩
```

* 运行npm命令执行打包

```js
npm run dev

```

* 创建index.html页面测试

```html
<body>
    <script src="./bundle.js"></script>
</body>
```

### 打包.css

实现步骤：

1. 安装转换css的组件
2. 修改webpack.config.js配置文件
3. 创建css文件
4. 修改入口文件，加载css文件
5. 打包测试运行编译命令

* 安装转换css的组件

> Webpack 本身只能处理 JavaScript 模块，如果要处理其他类型的文件，就需要使用 loader 进行转换。
>
> Loader 可以理解为是模块和资源的转换器。
>
> 安装相关Loader插件
>
> * css-loader 是将 css 装载到 javascript
> * style-loader 是让 javascript 认识css

```js
npm install --save-dev style-loader css-loader
```

* 修改webpack.config.js配置文件

```js
const path = require("path");     //导入path模块
module.exports = {        //定义JS打包的规则
    entry:"./src/main.js",
    output:{
        path:path.resolve(__dirname,"./dist"),
        filename:"bundle.js"
    },
    module:{         //定义css打包规则
        rules:[{
            test:/\.css$/,      //把项目中所有的.css结尾的文件进行打包
            use:["style-loader","css-loader"]
        }]
    }
}

```

* 创建css文件

```css
body{
    background: yellow;
    font-size: 64px;
    color:red;
}
```

* 修改入口文件，加载css文件

```js
const util = require("./util");     //导入util、common
const common = require("./common");
common.info("Helloword,"+util.add(100,100));
require("../style.css");      //导入css
```

* 打包测试运行编译命令

```shell
npm run dev
```

## Vue-element-admin后台前端解决方案

### 什么是脚手架

脚手架是指再软甲开发过程中，有人帮你把开发过程中要用到的工具、环境都配置好了，你就可以方便地直接开始做开发，专注你的业务，而不用再花时间去配置这个开发环境，这个开发环境就是脚手架。

### Vue-element-admin是什么

vue-element-admin 是一个后台前端解决方案，它基于 vue 和 element-ui实现。它使用了最新的前端技术栈，内置了 i18 国际化解决方案，动态路由，权限验证，提炼了典型的业务模型，提供了丰富的功能组件，它可以帮助你快速搭建企业级中后台产品原型。  
vue-element-admin 让后端程序员也能轻松上手做一些前端页面，而且配置打包都很简单。

官网网址：[https://panjiachen.github.io/vue-element-admin-site/zh/](https://panjiachen.github.io/vue-element-admin-site/zh/){target="_blank"}

**运行工程和编译工程**:

> 克隆项目：git clone[https://github.com/PanJiaChen/vue-element-admin.git](https://github.com/PanJiaChen/vue-element-admin.git){target="_blank"}
> 进入项目目录：cd vue-element-admin
> 安装依赖：npm install
> 如果安装慢可以使用：npm install --registry=<https://registry.npm.taobao.org>{target="_blank"}
> 本地开发 启动项目：npm run dev
> 启动完成后会自动打开浏览器访问[http://localhost:9527](http://localhost:9527/)

还历史以真诚，还生命以过程。 ——余秋雨
