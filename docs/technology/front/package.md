# 前端package.json介绍

原文: <https://docs.npmjs.com/cli/v8/configuring-npm/package-json>
翻译转自: <https://www.cnblogs.com/nullcc/p/5829218.html>

## **概述**

本文囊括了所有`package.json`文件中你需要知道的细节。注意`package.json`必须是纯JSON的，而不仅仅是一个JavaScript对象字面量。  
该文件描述的很多行为都受`npm-config`中的配置影响。

下面分别介绍`package.json`中各个字段的含义和用法。

<!-- more -->

## **name**

name和version字段是`package.json`文件中最重要的字段。这是必须的字段，如果你的npm包没有指定这两个字段，将无法被安装。name和version字段被假定组合成一个唯一的标识符。包内容的更改和包版本的更改是同步的。

name字段的含义不需要过多解释，就是npm包名。

几个规则：

1. name的长度必须小于等于214个字符。  
2. name不能以"."(点)或者"\_"(下划线)开头。  
3. name中不能包含大写字母。  
4. name最终将被用作URL的一部分、命令行的参数和文件夹名。因此，name不能含有非URL安全的字符。

几个建议：

1. 不要使用已存在的name作为包名。  
2. 不要在name中使用"js"和"node"，这会假定这是js文件，一旦你写一个`package.json`文件，你就可以在"engines"字段中指定解释器引擎。  
3. name字段可能会被作为传输传递给require()函数，因此它最好是简短的、自描述的。  
4. 你可能会需要在深入开发一个包之前先检查npm的registry来确认某个name是否被使用过，可以参考<https://www.npmjs.com/>。

一个name可以用scope来指定一个前缀，比如@myorg/mypackage，可以参考[npm-scope](https://docs.npmjs.com/misc/scope)。

## **version**

name和version字段是package.json文件中最重要的字段。这是必须的字段，如果你的npm包没有指定这两个字段，将无法被安装。name和version字段被假定组合成一个唯一的标识符。包内容的更改和包版本的更改是同步的。

version字段必须能够被[node-semver](https://github.com/isaacs/node-semver)解析，node-semver作为依赖项被捆绑进了npm中。(可以使用npm install semver来使用)

关于版本号和范围的信息可以参考[semver](https://docs.npmjs.com/misc/semver)。

## **description**

npm包的描述，description是一个字符串。它可以帮助人们在使用npm search时找到这个包。

## **keywords**

npm包的关键字，keywords是一个字符串的数组。它可以帮助人们在使用npm search时找到这个包。

## **homepage**

项目主页的url。

注意： 这和"url"不一样。如果你放一个"url"字段，registry会以为是一个跳转到你发布在其他地方的地址，然后鄙视你。

## **bugs**

改项目的issue跟踪页面或这报告issue的email地址。这对使用这个包遇到问题的用户会有帮助。

差不多是这样：

```json
{ 
　　"url" : "https://github.com/owner/project/issues",
　　"email" : "project@hostname.com"
}
```

你可以择其一或者两个都写上。如果只想提供一个url，你可以对"bugs"字段指定一个字符串而不是object。

如果提供了一个url，它会被用于npm bugs命令。

## **license**

你应该对你的包指定一个license来让用户知道他们的使用权利和和任何限制。

如果你正在使用BSD-2-Clause或MIT这样的通用许可证，可以为你的license添加一个当前SPDX的许可证标识符，比如：

```json
{ "license" : "BSD-3-Clause" }
```

你可以查看[SPDX许可证标识符的完整列表](https://spdx.org/licenses/)，理想情况下你应该挑选一个经过[OSI](https://opensource.org/licenses/alphabetical)核准的标识符。

如果你的包在多个通用许可证下被授权，使用一个[SPDX许可证表达式语法v2.0](https://npmjs.com/package/spdx)，比如：

```json
{ "license" : "(ISC OR GPL-3.0)" }
```

如果你正在使用的许可未被授予一个SPDX标识符，或者你正在使用自定义的许可证，使用如下：

```json
{ "license" : "SEE LICENSE IN <filename>" }
```

然后在包的根目录下提供一个叫的许可证文件。

一些旧的包使用license对象或一个"license"属性包含一个license的数组：

```json
// Not valid metadata
{ "license" :
    { 
        "type" : "ISC"，
        "url" : "http://opensource.org/licenses/ISC"
    }
}        
```

```json
//Notvalidmetadata
{
    "licenses": [
        {
            "type": "MIT",
            "url": "http://www.opensource.org/licenses/mit-license.php"
        },
        {
            "type": "Apache-2.0",
            "url": "http://opensource.org/licenses/apache2.0.php"
        }
    ]
}
```

上述这种风格的写法已经被废弃了，取而代之的是SPDX表达式：

```json
{ "license": "ISC" }

{ "license": "(MIT OR Apache-2.0)" }
```

最后，如果你不希望授权别人以任何形式使用私有包或未发布的包，可以这样写：

```json
{ "license": "UNLICENSED"}
```

也可以设置：

```json
"private": true
```

来防止意外的发布。

## **关于人的字段: author, contributors**

author是一个人，contributors是一些人的数组。person是一个对象，拥有必须的name字段和可选的url和email字段，像这样：

```json
{
    "name": "Barney Rubble",
    "email": "b@rubble.com",
    "url": "http://barnyrubble.tumblr.com/"
}
```

或者你也可以使用单个字符串的精简形式，npm会帮你解析它：

```shell
"Barney Rubble <b@rubble.com> (http://barnyrubble.tumblr.com/)"
```

这里email和url也是可选的。

npm也会使用你提供的npm用户信息来设置一个顶级的"maintainers"字段。

## **funding**

你可以指定一个包含 URL 的对象，该 URL 提供有关帮助资助包开发的方法的最新信息，或字符串 URL 或这些的数组：

```json
{
  "funding": {
    "type" : "individual",
    "url" : "http://example.com/donate"
  },

  "funding": {
    "type" : "patreon",
    "url" : "https://www.patreon.com/my-account"
  },

  "funding": "http://example.com/donate",

  "funding": [
    {
      "type" : "individual",
      "url" : "http://example.com/donate"
    },
    "http://example.com/donateAlso",
    {
      "type" : "patreon",
      "url" : "https://www.patreon.com/my-account"
    }
  ]
}
```

用户可以使用`npm fund`子命令列出他们项目的所有依赖项的`funding`URL，直接和间接的方式。 提供项目名称时也提供访问每个帮助网址的快捷方式，例如：`npm fund <projectname>`（当有多个网址时，将访问第一个）

## **files**

files字段是一个被项目包含的文件名数组，如果你在里面放一个文件夹名，那么这个文件夹中的所有文件都会被包含进项目中(除非是那些在其他规则中被忽略的文件)。

你还可以在包的根目录或子目录下提供一个".npmignore"文件来忽略项目包含文件，即使这些文件被包含在files字段中。.npmignore文件和.gitignore的功能很像。

某些文件总是被包含的，不论是否在规则中指定了它们：

```text
package.json  
README (and its variants)  
CHANGELOG (and its variants)  
LICENSE / LICENCE
```

相反地，一些文件总是被忽略：

```text
.git  
CVS  
.svn  
.hg  
.lock-wscript  
.wafpickle-N  
\*.swp  
.DS\_Store  
.\_\*  
npm-debug.log  
```
  
## **main**

main字段指定了模块的入口程序文件。就是说，如果你的模块名叫"foo"，用户安装了它，并且调用了 require("foo")，则这个main字段指定的模块的导出对象会被返回。

这应该是一个相对于包根目录的模块标识。

对于大部分模块来说，main字段除了指定一个主入口文件以外没什么其他用处了。

## **bin**

许多包有一个或多个可执行文件希望被安装到系统路径。在npm下要这么做非常容易(事实上，npm就是这么运行的)。

这需要在你的package.json中提供一个bin字段，它是一个命令名和本地文件名的映射。在安装时，如果是全局安装，npm将会使用符号链接把这些文件链接到prefix/bin，如果是本地安装，会链接到./node\_modules/.bin/。

比如，要使用myapp作为命令时可以这么做：

```json
{ "bin" : { "myapp" : "./cli.js" } }
```

这么一来，当你安装myapp，npm会从cli.js文件创建一个到/usr/local/bin/myapp的符号链接(这使你可以直接在命令行执行myapp)。

如果你只有一个可执行文件，那么它的名字应该和包名相同，此时只需要提供这个文件路径(字符串)，比如：

```json
{
    "name": "my-program",
    "version": "1.2.5",
    "bin": "./path/to/program"
}
```

这和以下这种写法相同：

```json
{
    "name": "my-program",
    "version": "1.2.5",
    "bin": {
        "my-program": "./path/to/program"
    }
}
```

## **man**

指定一个单一的文件名或一个文件名数组来让man程序使用。

如果只给man字段提供一个文件，则安装完毕后，它就是man 的结果，这和此文件名无关，比如：

```json
{
    "name": "foo",
    "version": "1.2.3",
    "description": "A packaged foo fooer for fooing foos",
    "main": "foo.js",
    "man": "./man/doc.1"
}
```

上面这个配置将会在执行man foo时就会使用./man/doc.1这个文件。

如果指定的文件名并未以包名开头，那么它会被冠以前缀，像这样：

```json
{
    "name": "foo",
    "version": "1.2.3",
    "description": "A packaged foo fooer for fooing foos",
    "main": "foo.js",
    "man": [
        "./man/foo.1",
        "./man/bar.1"
    ]
}
```

这将会为man foo和man foo-bar创建文件。

man文件必须以一个数字结尾，和一个可选的.gz后缀(当它被压缩时)。这个数字说明了这个文件被安装到哪个节中。

```json
{
    "name": "foo",
    "version": "1.2.3",
    "description": "A packaged foo fooer for fooing foos",
    "main": "foo.js",
    "man": [
        "./man/foo.1",
        "./man/foo.2"
    ]
}
```

会为使用man foo和man 2 foo而创建。

## **directories**

CommonJS Packages规范说明了几种你可以用directories对象来标示你的包结构的方法。如果你去看[npm's package.json](https://registry.npmjs.org/npm/latest)，你会看到它标示出出doc、lib和man。

在未来，这个信息可能会被用到。

## **directories.lib**

告诉你库文件夹的位置，目前没有什么地方需要用到lib文件夹，但是这是重要的元信息。

### **directories.bin**

如果你在directories.bin中指定一个bin目录，在这个目录中的所有文件都会被当做在bin来使用。

由于bin指令的工作方式，同时指定一个bin路径和设置directories.bin将是一个错误。如果你想指定独立的文件，使用bin，如果想执行某个文件夹里的所有文件，使用directories.bin。

### **directories.man**

directories.man指定的文件夹里都是man文件，系统通过遍历这个文件夹来生成一个man的数组。

### **directories.doc**

把markdown文件放在这。也许某一天这些文件将被漂亮地展示出来，不过这仅仅是也许。  
  
### **directories.example**

把示例脚本放在这。也许某一天会被用到。

## **repository**

指明你的代码被托管在何处，这对那些想要参与到这个项目中的人来说很有帮助。如果git仓库在github上，用npm docs命令将会找到你。

像这样：

```json
{
    "repository": {
        "type": "git",
        "url": "https://github.com/npm/npm.git"
    }
}
```

url应该是公开且可用的(可能是只读的)，这个url应该可以被版本控制系统不经修改地处理。不应该是一个在浏览器中打开的html项目页面，这个url是给计算机使用的。

对于github、github gist、Bitbucket或GitLab的仓库，你可以在npm install中使用相同的缩写形式：

```json
"repository": "npm/npm"
"repository": "gist:11081aaa281"
"repository": "bitbucket:example/repo"
"repository": "gitlab:another/repo"
```

## **scripts**

scripts字段是一个由脚本命令组成的字典，这些命令运行在包的各个生命周期中。这里的键是生命周期事件名，值是要运行的命令。可以参考[npm-scripts](https://docs.npmjs.com/files/package.json#directorieslib)获取配置scripts的更多信息。

## **config**

config字段是一个对象，可以用来配置包脚本中的跨版本参数，比如如下这个实例：

```json
{
    "name": "foo",
    "config": {
        "port": "8080"
    }
}
```

然后有一个start命令引用npm\_package\_config\_port环境变量，用户也可以用如下方式改写：

```shell
npm config set foo:port 8001
```

可以参考[npm-config](https://docs.npmjs.com/misc/config)和[npm-scripts](https://docs.npmjs.com/misc/scripts)获得更多关于包配置的信息。

## **dependencies**

dependencies字段是一个对象，它指定了依赖的包名和其版本范围的映射。版本范围是个有一个或多个空白分隔描述符的字符串。dependencies字段还可以用tarball或者git URL。

请不要将测试或过渡性的依赖放到dependencies中，请参考下面的devDependencies。

可以参考[semver](https://docs.npmjs.com/misc/semver)获取更多关于指定版本范围的细节信息。

1. `version` 必须确切匹配这个version  
2. `>version` 必须大于这个version  
3. `>=version` 必须大于等于这个version  
4. `< version` 必须小于这个version  
5. `<=version` 必须小于等于这个version  
6. `~version` 大约相当于version，参考[semver](https://docs.npmjs.com/misc/semver)  
7. `^version` 与version兼容，参考[semver](https://docs.npmjs.com/misc/semver)  
8. `1.2.x` 可以是`1.2.0`、`1.2.1`等，但不能是`1.3.0`
9. `http://...` 参考下面的URL作为依赖项  
10. `*` 匹配任何版本  
11. `""`(空字符串) 匹配任何版本，和`*`一样  
12. `version1 - version2` 相当于`>=version1 <=version2`
13. `range1 || range2 range1`或`range2`其中一个满足时采用该`version`
14. `git...` 参考下面的`Git URL`作为依赖项  
15. `user/repo` 参考下面的`GitHub URLs`
16. `tag` 一个以`tag`发布的指定版本，参考[npm-tag](https://docs.npmjs.com/cli/tag)  
17. `path/path/path` 参考下面的本地`Paths`

举个栗子，下面这种写法是合法的：

```json
{
    "dependencies": {
        "foo": "1.0.0 - 2.9999.9999",
        "bar": ">=1.0.2 <2.1.2",
        "baz": ">1.0.2 <=2.3.4",
        "boo": "2.0.1",
        "qux": "<1.0.0 || >=2.3.1 <2.4.5 || >=2.5.2 <3.0.0",
        "asd": "http://asdf.com/asdf.tar.gz",
        "til": "~1.2",
        "elf": "~1.2.3",
        "two": "2.x",
        "thr": "3.3.x",
        "lat": "latest",
        "dyl": "file:../dyl"
    }
}
```

### **URLs作为依赖项**

可以在version上指定一个压缩包的url。

当执行npm install时这个压缩包会被下载并且安装到本地。

### **Git URLs作为依赖项**

Git URLs可以是如下几种形式之一：

git://github.com/user/project.git#commit-ish  
git+ssh://user@hostname:project.git#commit-ish  
git+ssh://user@hostname/project.git#commit-ish  
git+<http://user@hostname/project/blah.git#commit-ish>  
git+<https://user@hostname/project/blah.git#commit-ish>  
  
commit-ish可以是任何tag、sha或者branch，并作为一个参数提供给git进行checkout，默认值是master。

### **GitHub URLs**

从1.1.65版本开始，你可以引用Github urls作为版本号，比如"foo": "user/foo-project"。也可以包含一个commit-ish后缀，举个栗子：

```json
{
    "name": "foo",
    "version": "0.0.0",
    "dependencies": {
        "express": "visionmedia/express",
        "mocha": "visionmedia/mocha#4727d357ea"
    }
}
```

### **本地路径**

从版本2.0.0开始你可以提供一个包的本地路径。本地路径可以在你使用npm install -S或npm install --save时被保存，具体形式如下：

* ../foo/bar  
* ~/foo/bar  
* ./foo/bar  
* /foo/bar  
  
在下面这种情况下它会被规范化成为一个相对路径并且加入到你的package.json文件中，比如：

```json
{
    "name": "baz",
    "dependencies": {
        "bar": "file:../foo/bar"
    }
}
```

这个特性有助于当你不想从一个外部服务器安装npm包的情况，比如本地离线开发和创建测试，但最好不要在发布包到公共registry时这样使用。

## **devDependencies**

如果有人计划在他们的项目中下载和使用你的模块，但他们可能并不想或并不需要你开发所使用的外部测试和文档框架。

在这种情况下，最好将这些附加的项放在devDependencies中。

这些项将会在根目录下执行npm link或npm install时被安装，并且可以像其他npm配置参数一样被管理。可以参考[npm-config](https://docs.npmjs.com/misc/config)获得更多信息。

对于那些非特定平台的构建步骤，比如编译CoffeeScript或把其他语言转换成JavaScript，可以使用prepublish脚本来处理，并且把这个过程的依赖包放在devDependencies中。

举个栗子：

```json
{
    "name": "ethopia-waza",
    "description": "a delightfully fruity coffee varietal",
    "version": "1.2.3",
    "devDependencies": {
        "coffee-script": "~1.6.3"
    },
    "scripts": {
        "prepublish": "coffee -o lib/ -c src/waza.coffee"
    },
    "main": "lib/waza.js"
}
```

prepublish脚本会在publishing前运行，这样用户就可以不用自己去require来编译就能使用。在开发模式下(比如本地运行npm install)，将会执行这个脚本，这样测试就非常方便了。

## **peerDependencies**

在某些情况下，当一个主机无法require依赖包时，你会想要告诉它还有哪些工具或库与这个依赖包兼容。这通常被成为一个插件。尤其是在host文档中声明的模块会暴露一个特定的接口。

举个栗子：

```json
{
    "name": "tea-latte",
    "version": "1.3.5",
    "peerDependencies": {
        "tea": "2.x"
    }
}
```

这将确保tea-latte这个包只会和2.x版本的tea一起被安装。执行npm install tea-latte可能产生以下关系图：

├── tea-latte@1.3.5  
└── tea@2.2.0

注意：如果没有在依赖树中显式声明比它们更高的依赖版本，版本1和版本2的npm将会自动安装peerDependencies。在npm的下一个大版本npm3中，情况将完全不同。你将收到一个警告，告诉你peerDependency还没有被安装。在npm1和npm2中这个行为经常会导致混乱，新的npm版本的设计将会极力避免这种情况。

试图安装一个有冲突的依赖项的插件将会导致一个错误。因此你必须确保你的插件的依赖项版本范围尽可能大，并且不要把版本锁死在一个特点的补丁版本上。

假设主机使用semver进行编译，只改变这个包的主版本将会导致你的插件不可用。因此，如果你的插件的某个依赖包运行在每个1.x版本下，使用"^1.0"或"1.x"。如果你需要的功能在1.5.2版本中，使用">= 1.5.2 < 2"。

## **bundledDependencies**

在发布包时，包名的数组会被打包进去。

如果拼写成"bundleDependencies"(少个d)，也是可以的。

## **optionalDependencies**

如果一个依赖项可用，但希望在这个依赖项无法被找到或者安装时失败npm还能继续处理(不中断)，那么你可以把它放在optionalDependencies中。和dependencies一样，optionalDependencies是一个包名和版本号或url的映射。区别在于optionalDependencies中的依赖构建失败时不会导致npm整体安装失败。

但是你的程序依然有责任处理这种缺失的依赖项，比如这样：

```js
try{
    varfoo=require('foo')varfooVersion=require('foo/package.json').version
}catch(er){
    foo=null
}if(notGoodFooVersion(fooVersion)){
    foo=null
}//..thenlaterinyourprogram..if(foo){
    foo.doFooThings()
}
```

optionalDependencies中的项会覆盖dependencies中的同名项，所以一个特定名字的项最好只出现在一个地方。

## **engines**

你可以指定node的工作版本：

```json
{ "engines" : { "node" : ">=0.10.3 <0.12" } }
```

和dependencies类似，如果你不指定一个node版本(或者你用'\*'指定)，则任何一个node版本都可以。

如果你指定了一个'engines'字段，则npm将会在某处包含这个node版本。如果忽略'engines'字段，则npm只会仅仅假设这个包工作在node下。

你还可以使用'engines'字段来指定可以安装这个包的npm版本，举个栗子：

```json
{ "engines" : { "npm" : "~1.0.20" } }
```

请注意，除非用户设置了engine-strict标记，否则这个字段只是一个建议值。

## **engineStrict**

这个特性在npm 3.0.0中已经废弃。

npm 3.0.0之前的版本，这个特性用来处理那些设置了engine-strict标记的包。

## **os**

可以指定模块运行的操作系统：

```json
"os" : [ "darwin", "linux" ]
```

也可以使用操作系统黑名单来替代白名单，只要在前面加个'!'：

```json
"os" : [ "!win32" ]
```

主机的操作系统可以通过process.platform来确定。

虽然找不到什么很好的理由支持这么做，但是这里还可以黑名单和白名单混用。

## **cpu**

如果你的代码只能运行在特定的cpu架构上，你可以指明：

```json
"cpu" : [ "x64", "ia32" ]
```

和os选项类似，你还可以使用黑名单：

```json
"cpu" : [ "!arm", "!mips" ]
```

主机的cpu架构可以通过process.arch来确定。

## **preferGlobal**

如果你的包是一个需要进行全局安装的命令行应用，需要设置preferGlobal为true，如果这个包被本地安装会报出一个警告。

这个选项并不会阻止用户本地安装这个包，但这么做确实能在包未按照预期被安装造成诸多麻烦时提供一些提示。

## **private**

如果你在包的package.json中设置"private": true，则npm会拒绝发布它。

这是防止私有包被以外发布的一种方法。如果你希望包装某个包只能被发布到特定的一个registry中(比如，一个内部的registry)，则可以使用下面的publishConfig字典来描述以在publish-time重写registry配置参数。

## **publishConfig**

这是一个在publish-time时会用到的配置集合。当你想设置tag、registry或access时特别有用，所以你可以确保一个给定的包无法在没有被打上"latest"标记时就被发布到全局公共的registry。

任何配置都可以被覆盖，当然可能只有"tag", "registry"和"access"和发布意图有关。

参考[npm-config](https://docs.npmjs.com/misc/config)来查看那些可以被覆盖的配置项列表。

## **DEFAULT VALUES**

npm会基于包内容设置一些默认值。

```json
"scripts": {"start": "node server.js"}
```

如果包的根目录中有一个server.js，那么npm会用它来作为入口文件：运行node server.js。

```json
"scripts":{"preinstall": "node-gyp rebuild"}
```

如果包的根目录中有一个binding.gyp文件，那么npm会在运行preinstall命令编译时使用它。

```json
 "contributors": [...]
```

如果包的根目录中有一个AUTHORS文件，那么npm会把它的每一个行格式化成Name \\ (url)的形式，其中email和url是可选的。以一个#或者空白符开头的行将被忽略。

## **参考资料**

* [semver](https://docs.npmjs.com/misc/semver){target="_blank"}
* [npm-init](https://docs.npmjs.com/cli/init){target="_blank"}
* [npm-version](https://docs.npmjs.com/cli/version){target="_blank"}
* [npm-config](https://docs.npmjs.com/cli/config){target="_blank"}
* [npm-config](https://docs.npmjs.com/misc/config){target="_blank"}
* [npm-help](https://docs.npmjs.com/cli/help){target="_blank"}
* [npm-faq](https://docs.npmjs.com/misc/faq){target="_blank"}
* [npm-install](https://docs.npmjs.com/cli/install){target="_blank"}
* [npm-publish](https://docs.npmjs.com/cli/publish){target="_blank"}
* [npm-uninstall](https://docs.npmjs.com/cli/uninstall){target="_blank"}
