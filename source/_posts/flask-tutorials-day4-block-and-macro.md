---
title: Flask系列学习笔记-Day4-Flask Jinja2模板之Block-Macro-Include
date: 2020-10-30 07:33:16
categories: 
  - flask
description: Jinja2提供了块 (Block)和宏 (Macro)的功能。块功能有些类似于C语言中的宏，原理就是代码替换；而宏的功能有些类似于函数，可以传入参数。
tags: 
  - Flask
---

Jinja2提供了块 (Block)和宏 (Macro)的功能。块功能有些类似于C语言中的宏，原理就是代码替换；而宏的功能有些类似于函数，可以传入参数；Include是可以直接包含整个模板。

### 块 (Block)

**形象理解`Block`: 模板就是一篇文章，`Block`就是文章里的括号`( )`，我们需要往`( )`里面填进内容**。也即是说我们有个初始模板如`layout.html`在里面定义了一堆`Block`, 然后在其他前端页面中：

1. 使用 `{ % extends "layout.html" % }`来继承该模板
2. 将需要填的空补齐`block name` --> `endblock`
3. **基础`layout.html`中可能存在比较多的`Block`，如果子模板中没有填充该`Block`，则不会继承覆盖该`Block`**

不过要注意几个点：

1. 模板不支持多继承，也就是子模板中定义的块，不可能同时被两个父模板替换。
2. 模板中不能定义多个同名的块，子模板和父模板都不行，因为这样无法知道要替换哪一个部分的内容。

另外，我们建议在`endblock`关键字后也加上块名，比如`endblock block_name `。虽然对程序没什么作用，但是当有多个块嵌套时，可读性好很多。

#### 保留父模板块的内容

如果父模板中的块里有内容不想被子模板替换怎么办？可以使用`super()`方法。如父模板"layout.html"为：

```html
<!doctype html>
<head>
    {% block head %}
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>{% block title %}{% endblock %}</title>
    {% endblock %}
</head>
<body>
    <div class="page">
    {% block body %}
    {% endblock %}
    </div>
</body>
```

并在子模板里，加上"head"块和"title"块：

```html
{% block title %}Block Sample{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        h1 { color: #336699; }
    </style>
{% endblock %}
```

父模板同子模板的"head"块中都有内容。运行后，你可以看到，父模板中的"head"块语句先被加载，而后是子模板中的"head"块语句。这就得益于我们在子模板的"head"块中加上了表达式`{ { super() } }`。效果有点像Java中的`super()`吧。

#### 块内语句的作用域

默认情况下，块内语句是无法访问块外作用域中的变量。比如我们在"layout.html"加上一个循环：

```html
{% for item in range(5) %}
   <li>{% block list %}{% endblock %}</li>
{% endfor %}
```

然后在子模板中定义"list"块并访问循环中的"item"变量：

```html
{% block list %}
    <em>{{ item }}</em>
{% endblock %}
```

你会发现页面上什么数字也没显示。如果你想在块内访问这个块外的变量，你就需要在块声明时添加`scoped`关键字。比如我们在"layout.html"中这样声明"list"块即可：

```html
    {% for item in range(5) %}
        <li>{% block list scoped %}{% endblock %}</li>
    {% endfor %}
```

### 宏 (Macro)

凭借将反复出现的代码片段抽象成**宏**，我们可以实现DRY原则（Don't Repeat Yourself）。宏类似于函数。既然是函数就有其声明和调用两个部分。

先声明一个表单宏：

templates/form.html

```html
{% macro input(name, type='text', value='') -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}">
{%- endmacro %}
```

上面定义了一个宏，名称是input，这个宏有三个参数，分别是name、type、value，下面调用它：

templates/hello-6.html

```html
{% import 'form.html' as form %}
<p>{{ form.input('username', value='user') }}</p>
<p>{{ form.input('password', 'password') }}</p>
<p>{{ form.input('submit', 'submit', 'Submit') }}</p>
{% from 'form.html' import input %}
<p>{{ input('username', value='user') }}</p>
<p>{{ input('password', 'password') }}</p>
<p>{{ input('submit', 'submit', 'Submit', 'more arg1', 'more arg2', ext='more arg3') }}</p>
```

可以在页面上看到一个文本输入框，一个密码输入框及一个提交按钮。是不是同函数一样啊？其实它还有比函数更丰富的功能，之后我们来介绍。

#### 访问调用者内容

我们先来创建个宏"list_users"：

```html
{% macro list_users(users) -%}
  <table>
    <tr><th>Name</th><th>Action</th></tr>
    {%- for user in users %}
      <tr><td>{{ user.name |e }}</td>{{ caller() }}</tr>
    {%- endfor %}
  </table>
{%- endmacro %}
```

宏的作用就是将用户列表显示在表格里，表格每一行用户名称后面调用了`{ { caller( ) } }`方法，这个有什么用呢？先别急，我们来写调用者的代码：

```html
{% set users=[{'name':'Tom','gender':'M','age':20},
              {'name':'John','gender':'M','age':18},
              {'name':'Mary','gender':'F','age':24}]
%}

{% call list_users(users) %}
    <td><input name="delete" type="button" value="Delete"></td>
{% endcall %}
```

与上例不同，这里我们使用了`{ % call % }`语句块来调用宏，语句块中包括了一段生成"Delete"按钮的代码。运行下试试，你会发现每个用户名后面都出现了"Delete"按钮，也就是`{ { caller( ) } }`部分被调用者`{ % call % }`语句块内部的内容替代了。不明觉厉吧！其实吧，这个跟函数传个参数进去没啥大区别，个人觉得，主要是有些时候HTML语句太复杂（如上例），不方便写在调用参数上，所以就写在`{ % call % }`语句块里了。

Jinja2的宏不但能访问调用者语句块的内容，还能给调用者传递参数。嚯，这又是个什么鬼？我们来扩展下上面的例子。首先，我们将表格增加一列性别，并在宏里调用`caller()`方法时，传入一个变量`user.gender`：

```html
{% macro list_users(users) -%}
  <table>
    <tr><th>Name</th><th>Gender</th><th>Action</th></tr>
    {%- for user in users %}
      <tr><td>{{ user.name |e }}</td>{{ caller(user.gender) }}</tr>
    {%- endfor %}
  </table>
{%- endmacro %}
```

然后，我们修改下调用者语句块：

```html
{% call(gender) list_users(users) %}
    <td>
    {% if gender == 'M' %}
    <img src="{{ url_for('static', filename='img/male.png') }}" width="20px">
    {% else %}
    <img src="{{ url_for('static', filename='img/female.png') }}" width="20px">
    {% endif %}
    </td>
    <td><input name="delete" type="button" value="Delete"></td>
{% endcall %}
```

大家注意到，我们在使用`{ % call % }`语句时，将其改为了`{ % call(gender) ... % }`，这个括号中的`gender`就是用来接受宏里传来的`user.gender`变量。因此我们就可以在{ % call % }语句中使用这个`gender`变量来判断用户性别。这样宏就成功地向调用者传递了参数。

#### 宏的内部变量

上例中，我们看到宏的内部可以使用`caller( )`方法获取调用者的内容。此外宏还提供了两个内部变量：

- varargs
  这是一个列表。如果调用宏时传入的参数多于宏声明时的参数，多出来的**没指定参数名**的参数就会保存在这个列表中。
- kwargs
  这是一个字典。如果调用宏时传入的参数多于宏声明时的参数，多出来的**指定了参数名**的参数就会保存在这个字典中。

让我们回到第一个例子`input`宏，在调用时增加其传入的参数，并在宏内将上述两个变量打印出来：

```html
{% macro input(name, type='text', value='') -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}">
    <br /> {{ varargs }}
    <br /> {{ kwargs }}
{%- endmacro %}
<p>{{ input('submit', 'submit', 'Submit', 'more arg1', 'more arg2', ext='more arg3') }}</p>
```

可以看到，`varargs`变量存了参数列表`['more arg1', 'more arg2']`，而kwargs字典存了参数`{'ext':'more arg3'}`。

#### 宏的导入

一个宏可以被不同的模板使用，所以我们建议将其声明在一个单独的模板文件中。需要使用时导入进来即可，而导入的方法也非常类似于Python中的”import”。让我们将第一个例子中”input”宏的声明放到一个”form.html”模板文件中，然后将调用的代码改为：

```python
{% import 'form.html' as form %}
<p>{{ form.input('username', value='user') }}</p>
<p>{{ form.input('password', 'password') }}</p>
<p>{{ form.input('submit', 'submit', 'Submit') }}</p>
```

运行下，效果是不是同之前的一样？你也可以采用下面的方式导入：

```python
{% from 'form.html' import input %}
<p>{{ input('username', value='user') }}</p>
<p>{{ input('password', 'password') }}</p>
<p>{{ input('submit', 'submit', 'Submit') }}</p>
```

### 包含 (Include)

这里我们再介绍一个Jinja2模板中代码重用的功能，就是包含 (Include)，使用的方法就是`{ % include % }`语句。其功能就是将另一个模板加载到当前模板中，并直接渲染在当前位置上。它同导入"import"不一样，"import"之后你还需要调用宏来渲染你的内容，"include"是直接将目标模板渲染出来。它同block块继承也不一样，它一次渲染整个模板文件内容，不分块。

我们可以创建一个"footer.html"模板，并在"layout.html"中包含这个模板：

```html
<body>
    ...
    {% include 'footer.html' %}
</body>
```

当"include"的模板文件不存在时，程序会抛出异常。你可以加上`ignore missing`关键字，这样如果模板不存在，就会忽略这段`{ % include % }`语句。

```python
{% include 'footer.html' ignore missing %}
```

{ % include % }语句还可以跟一个模板列表：

```python
{% include ['footer.html','bottom.html','end.html'] ignore missing %}
```

上例中，程序会按顺序寻找模板文件，第一个被找到的模板即被加载，而其后的模板都会被忽略。如果都没找到，那整个语句都会被忽略。

[day4完整demo代码下载](download/day4-demo.zip)