---
title: 使用GitHub与Gitbook制作自己的书籍
date: 2018-08-13 11:05:44
updated: 2018-08-13 11:05:44
description: 最近在学习网络爬虫知识，经常需要做笔记，有几个选择。Hexo博客记录：还是不太喜欢这种定制化过高的博客，等有时间了再来自己折腾一个出来，Pass。 有道笔记：还算是好用，但是每次记录或者查询的时候都要登录显得不是那么方便，Pass。 GitHub：可以在任意地方查阅与修改，是很方便，但是网页形势浏览不是很方便，Pass。 Gitbook：可以在任意地方查阅与修改，web界面式浏览，很方便，就是它了。
categories: 
	- Web
tags:
	- Gitbook
	- Github
	- Git
	- Hexo
cover: https://cdn.jsdelivr.net/gh/meixuhong/cdn@master/img-hosting/gitbook.png
---

最近在学习网络爬虫知识，经常需要做笔记，有几个选择。

- Hexo博客记录：还是不太喜欢这种定制化过高的博客，等有时间了再来自己折腾一个出来，Pass。
- 有道笔记：还算是好用，但是每次记录或者查询的时候都要登录显得不是那么方便，Pass。
- GitHub：可以在任意地方查阅与修改，是很方便，但是网页形势浏览不是很方便，Pass。
- Gitbook：可以在任意地方查阅与修改，web界面式浏览，很方便，就是它了。

如果将Gitbook与GitHub结合起来，即是将`Book(笔记)`与GitHub中的`Repository`绑定起来，这样便可以在任意地方通过`Git`拉取仓库，修改内容，提交内容，GitBook会自动从GitHub中同步`Book(笔记)`。

# 1.gitbook生成本地书籍

## 1.1 安装gitbook

gitbook依赖`nodejs`，安装完成之后安装`gitbook`.

```shell
$ node --version
$ npm -v
$ npm install gitbook-cli -g
```

## 1.2 初始化book

```shell
$ gitbook init #会在当前目录生成两个文件， README.md和SUMMARY.md
$ gitbook serve #编译和预览书籍，实际上会首先调用 gitbook build 编译书籍,然后打开web服务器
```

`gitbook init`会在当前目录生成两个文件。

- README.md: 简介文档。
- SUMMARY.md: 定义了book的**目录结构，非常重要**。

`gitbook serve`命令会调用`gitbook build`在本地生成一个`_book`目录，这个目录就是一个静态站点，打开里面的**index.html**就可以访问本地book了。

## 1.3 在个人站点调用Book 

如果有个人站点，需要连接一个gitbook书籍，非常简单，只需要把上面通过`gitbook build`生成的`_book`目录放入相应位置即可，以Hexo为例。

我们知道发布Hexo博客有如下几个步骤。

- hexo clean: 清除cache文件。
- hexo g: 生成public文件，即Hexo站点静态文件。
- hexo d: 发布public站点到github或者其他托管站点。

我们只需要在`hexo g`命令执行完之后拷贝Gitbook的`_book`内容到Hexo的`public`目录，然后再执行`Hexo d`发布站点即可，访问Hexo站点的时候访问书籍的话通过网址：`xxx.github.io/_book`,浏览器就会自动调用该目录下的`index.html`文件。也可以尝试将下述命令做成可执行脚本直接运行。

```bash
$ hexo clean && hexo g && cp -fr ../[path]/_book/ public/ && hexo d
```

# 2. 发布Book到GitBook.com

## 2.1. 在Github中创建一个新的仓库

如果没有Github账号则新创建一个，然后创建一个新的仓库如，`ebook`

## 2.2. 在GitBook中注册一个新的账号

新版本[Gitbook](https://gitbook.com)注册后需要创建一个`organization`，为便于记忆，填写为个人名字即可。依照提示继续填入`project`,在`project`里面可以创建多个`space`，每个`space`便是一本书。

## 2.3. 绑定Gitbook与GitHub仓库

- 首先需要将Gitbook账号与GitHub账号进行绑定

![gitbook](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/Gitbook-Github.jpg)

- 关联账号后可以将书籍与仓库进行绑定关联

  进入`Space`后点击**设置**按钮进行关联前面创建的仓库`ebook`

![gitbook](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/Gitbook_integration.jpg)

## 2.4. 通过Git更新书籍

### 2.4.1 获取到`git`地址拷贝到本地

```shell
git clone git@github.com:wowmarcomei/ebook.git
```

### 2.4.2 添加`readme.md`与`summary.md`内容

```shell
gitbook init #生成README.md与SUMMARY.md
vi README.md #编辑README.md
vi SUAMMRY.md #这一步尤其重要，因为需要通过这个文件指定书籍的文档结构
git add *
git commit -m "Initial Commit"
git push origin master
```

即可将写好的`readme`内容推送到Github，Gitbook也会同步从Github中获取到数据。

### 2.4.3 编辑内容并推送到托管仓库

- 创建新章节：创建一个目录。
- 章节中的小章节：对应一个Markdown文件。
- 如果需要对章节进行多层嵌套，则嵌套创建目录即可。
- 编辑`SUMMARY.md`文件指定结构。

示例，新增一个章节，在里面指定对应小节：

```shell
mkdir 1.爬虫准备
vi 1.常见的三种数据库的安装配置.md
vi 2.Python常用库的安装.md
vi 3.使用Python的正则表达式过滤字符串.md
vi 4.理解Python中使用yield进行迭代.md
###编辑完内容后编辑SUMMARY.md文件指定目录结构
```

上述是使用vi命令编辑Markdown文件，实际上更推荐使用一些可视化的工作编辑，比如`typora`等等。

`SUMMARY.md`格式如下：

```shell
# Summary

* [Introduction](README.md)
* [1.准备工作](1.准备工作/README.md)
	* [1.常见的三种数据库的安装配置](1.准备工作/1.常见的三种数据库的安装配置.md)
	* [2.Python常用库的安装](1.准备工作/2.Python常用库的安装.md)
	* [3.使用Python的正则表达式过滤字符串](1.准备工作/3.使用Python的正则表达式过滤字符串.md)
	* [4.理解Python中使用yield进行迭代](1.准备工作/4.理解Python中使用yield进行迭代.md)
		* [1.爬虫基本流程](2.理解爬虫/1.爬虫基本流程.md)
		* [2.Python使用Urllib库爬取数据](2.理解爬虫/2.Python使用Urllib库爬取数据.md)
```

即为`[]()`构成的列表，如果需要嵌套层级，相比上一个层级多缩进一下即可，上面的例子中就有三个层级。

![gitbook](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/Gitbook-Structure.jpg)

完成后通过`git`推送到`github`,`gitbook.com`就会从仓库里自动同步，此时访问gitbook.com即可访问发布的数据。

```shell
$ git add *
$ git commit -m "update..."
$ git push origin master #推送到master分支，gitbook应该也是绑定到仓库的该分支，否则不能同github同步
```

![gitbook](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/Gitbook_overview.jpg)

> **瑕疵**: 新版本的Gitbook中对`Markdown`的有序列表支持不是很好，原本的列表项`1, 2, 3, 4, ... `在gitbook中会变成`1, 1, 1, 1, ...`，目前没看到有解决，所以我们在记录笔记的时候换成无序列表吧，或者换成小标题也行。