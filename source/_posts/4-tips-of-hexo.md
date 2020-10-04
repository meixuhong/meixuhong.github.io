---
title: Hexo的一些小技巧
date: 2016-07-19 07:24:36
categories: 
  - web
  - hexo
tags: 
    - Hexo
    - 折腾  
description: 在不断折腾自己开发Django、Flask、部署wordpress后，最终还是回到了Hexo，因为Hexo配合Github可以无需购买任何云服务器就可以方便部署个人静态站点，且可以通过git版本分布式管理的方式同步管理，使得成本与便携性兼具。

---

在不断折腾自己开发Django、Flask、部署wordpress后，最终还是回到了Hexo，因为Hexo配合Github可以无需购买任何云服务器就可以方便部署个人静态站点，且可以通过git版本分布式管理的方式同步管理，使得成本与便携性兼具。

本文记录Hexo使用过程中的一些小技巧，包括自定义html文件，为文章添加微信公众号，创建页面/菜单，编辑主题，修改字体等，后续不定期更新。

# 1. Hexo自定义html文件

> 注： Hexo生成的md文件最终都会转换为html文件，不过已经由Hexo渲染过。

有时候我们想自定义html页面，不经过Hexo渲染。可以先使用新建页面命令`hexo new page "about"`，这时会在source目录下生成about/about.md文件。可以将其修改为html文件，同时在文件头加上`layout: false`即可。

```bash
mv source/about/index.md source/about/index.html

```

编辑index.html文件时在头部加上`layout: false`后使用，编辑自己的html代码即可，eg:


```html
---

title: about

date: 2016-08-07 06:35:00

layout: false

---

<html lang="en">

<head>

  <title>Marco FreeCodeCamp_Ex1</title>

  <meta charset="utf-8">

  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<head>


<body>

</body>

</html>
```

# 2. 为每篇文章添加微信或者公众号

修改next主题下的config.yml文件，将注释部分去掉

```python
# Wechat Subscriber

wechat_subscriber:

  enabled: true

  qcode: /images/wechat.jpg

  description: welcome to scan my public wechat account

```

> 其中，需要将你微信或者公众号二维码加上传到source/images下。

# 3. 创建新的菜单

## 3.1  创建新页面

输入命令：

```bash
hexo new page "project"
```


此时会自动在source/about目录下生成新的目录project，且此目录下会生成index.md文件

添加type类型为project如：

```phython
---

title: project

date: 2016-08-07 10:11:05

type: "project"

---

```

## 3.2 编辑主题Menu

> 编辑主题目录下的_config.yml文件的menu选项，添加project并设置其icon

```phython
menu:

  home: /

  categories: /categories

  about: /about

  archives: /archives

  project: /project


menu_icons:

  enable: true

  #KeyMapsToMenuItemKey: NameOfTheIconFromFontAwesome

  home: home

  about: user

  categories: th

  tags: tags

  archives: archive

  project: heartbeat

```

## 3.3 修改字体
> 修改themes/next/language/zh-Hans.yml 中的menu选项，添加project

```phython
menu:

  home: 首页

  archives: 归档

  categories: 分类

  tags: 标签

  about: 关于

  search: 搜索

  commonweal: 公益404

  project:  项目

```

## 3.4 编辑页面

> 新建一篇文章,编辑项目文档

```bash
hexo new "project1"
```

这时会生成source/project/index.md文件，将其修改为source/project/index.html文件，后编写html文件即可

# 4. SEO Hexo站点

## 4.1 优化url

hexo默认url是年/月/日，这样其实不利于SEO。hexo生成新文章命令，hexo new [layout] <title>，这个title最好是英文的，因为我们要把这个title放在url里，如何修改这个title呢？那就是去source文件夹里直接修改.md文件名即可。但我们想让我们文章的标题显示中文的，这样如何修改呢？那就是在每篇文章的.md上方直接修改title为中文即可。

  - 创建文章时使用命令指定文章名
    `hexo new "How to make a beautiful URL in Hexo site"`  

  - 修改文件的title

   打开在source目录下的"How-to-make-a-beautiful-URL-in-Hexo-site.md"文件，修改title为自己想要取的中文名。

  - 修改hexo的配置文件`_config.yml`

   在根目录的配置文件中指定url的格式：

   ```bash
   # URL
   ## If your site is put in a subdirectory, set url as 'http://yoursite.com/child' and root as '/child/'
   url: http://meixuhong.cn
   root: /
   permalink: :year/:title/
   permalink_defaults:
   ```

   其中`root`指定了网站的根目录为`/`，`permalink`指定了文章的url为`:year/:title/`，此处之所以加了`year`是因为想在网站代码中格式更统一，后续有更好的选择的时候可以删除`year`关键字。

