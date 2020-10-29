---
title: Flask系列学习笔记-Day2-Flask之Jinja2模板
date: 2020-10-28 07:00:23
categories: 
  - flask
description: 应用Flask模板，我们可以快速开发出美观好看的前端页面，我们可以将模板看成MVC模式中的View视图层，而模板引擎（基本都是使用的Jinja2模板）来将模板同业务代码分离，并解析模板语言的程序。使用模板，可以减少flask项目代码的耦合性，页面逻辑放在模板中，业务逻辑放在视图函数中，将页面逻辑和业务逻辑解耦有利于代码的维护。
tags: 
  - Flask
---


# # 后端使用模板基本方法

先来看下模板的基本使用方法。

- 使用模板之前需要导入`render_template`支持库
```python
from flask import Flask,render_template
```

- 默认`html`模板放在templates下面
- 在路由(视图)函数里指定渲染，变量为templates里的文件名字符串，如`index.html`
```python
return render_template('index.html')
```

#  # Jinja语法规则

- 变量使用双括号`{{ }}`来定义，如`{{ movies}}`, 这个变量传递到路由函数里去

- `if`, `for`等语句使用`{%  %}`来指定，如`{% if movies %}`

- `Jinja`模板中使用注释的话，需要以`{# 这是注释部分 #}`进行

- 路由函数(也叫视图函数)中返回`render_template`进行渲染,可以指定参数，参数是传递给`html`模板中的变量，如：

  ```python
  render_template('index.html',name=user)
  # 其中`name`是传递到html模板index.html里的变量`{{name}}`,其值为user值
  ```

- `render_template`可以传递普通变量，也可以传递列表，字典

  ```python
  def index():
      user = {'nickname': 'Miguel'} # fake user
      posts = [# fake array of posts
          {
              'author': { 'nickname': 'John' },
              'body': 'Beautiful day in Portland!'
          },
          {
              'author': { 'nickname': 'Susan' },
              'body': 'The Avengers movie was so cool!'
          }
      ]     
      #title,user,posts是传递到html里的变量，右边的值是从本函数中获取到的
      return render_template('index.html',
          title = 'Home',
          user = user,
          posts = posts
      )
  ```

  
  
# # 使用url_for()函数

## 使用url_for做反转路由，即获取或者生成url地址

`url_for`函数既可以在后端`python`中使用，也可以在`Jinja`模板中使用。


### 在后端Python程序中使用`url_for`

 `url_for`: `url_for`的第一个参数是一个视图函数(也即是路由函数)的名字的字符串格式, 后面的参数的参数以关键字的形式传递给`url`。 **如果传递的参数在那个视图中`url`中定义了，那么这个参数就会以路径参数的形式给`url`。 如果传递的参数没有在`url`中定义，那么这些参数将会以查询字符串的形式放到`url`中**。

```python
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    my_list_path = url_for('my_list', page=1, count=111)
    print(my_list_path)       # 结果为： /list/1/?count=111，page在视图函数my_list(也称之为路由函数)中定义了，所以直接传递，count没有定义，故以查询字符串的形式放在url中
    return my_list_path

@app.route('/list/<int:page>/')
def my_list(page):
    return '第 {} 页'.format(page)
```

### 	在前端模板中使用`url_for`

> 模板中的`url_for`跟后台视图函数中的`urf_for`使用起来基本一模一样的，也是传递视图函数的名字，也可以传递参数，不同与后端Python之处在于**需要在`url_for`左右两边加上一个`{{ }}`**。

**如果传递的参数在那个视图中`url`中定义了，那么这个参数就会以路径参数的形式给`url`。 如果传递的参数没有在`url`中定义，那么这些参数将会以查询字符串的形式放到`url`中**。

如：在视图函数login()中定义`/mei/login/<id>/`：

```python
@app.route('/mei/login/<id>/')
def login(id):
    # print(id)
    return render_template('index.html')
```

在`Jinja`模板中通过`url_for`传递参数,其中第一个参数`login`是Flask中定义的视图函数, `id`是`login`函数参数，`ref`没有定义将会以查询字符串的形式传递, 所以最终生成的`url`为`login`视图函数里的`url`: `/mei/login/1/?ref=123`
```html
<p><a href="{{ url_for('login',ref='123',id=1)}}">登录</a></p>
```
另，加载静态文件使用的`url_for`函数，第一个参数需要为`'static'`, 第二个参数需要为一个关键字参数`filename='静态文件路径'`。
`static`为默认函数，无需自己重写，`filename`是该函数的参数。如下示例，可以直接引用得到`/static/css/index.css`这个`url`：

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
```

在对应的python文件中定义的视图函数`static`定义参数`filename`;路径查找，使用当前项目的`static`目录作为根目录。

> 强烈建议以后在使用`url`的时候，使用**`url_for`**来反转` url`

[完整demo代码下载](download/day2-Flask_demo.zip)

demo效果：

![](https://cdn.jsdelivr.net/gh/meixuhong/cdn//img/day2-1.jpg)

![](https://cdn.jsdelivr.net/gh/meixuhong/cdn//img/day2-2.jpg)

![](https://cdn.jsdelivr.net/gh/meixuhong/cdn//img/day2-3.jpg)



