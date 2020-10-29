---
title: Flask系列学习笔记-Day3-Flask Jinja2模板之过滤器
date: 2020-10-29 07:03:20
categories: 
  - flask
description: 过滤器其实就是一种转换函数，输入的参数就是其所修饰的变量，返回的就是变量转换后的值。
tags: 
  - Flask
---


###  使用过滤器

先看一个简单的例子：

```html
<h1>Hello {{ name | upper }}!</h1>
```

其中`name`就是在flask中定义的变量，最终过滤效果为变量`name`经过滤后最终均变成了大写。

在模板中该变量后面加上`|`符号，再加上过滤器名称，就可以对该变量作过滤转换。过滤器也可以连续使用：

```html
<h1>Hello {{ name | upper | truncate(3, True) }}!</h1>
```

现在`name`变量不但被转换为大写，而且当它的长度大于3后，只显示前3个字符，后面默认用”…“显示。过滤器`truncate`有3个参数，第一个是字符截取长度；第二个决定是否保留截取后的子串，默认是`False`，也就是当字符大于3后，只显示”…“，截取部分也不出现；第三个是省略符号，默认是”…“。

**过滤器本质上就是一个转换函数，它的第一个参数就是待过滤的变量，在模板中使用时可以省略去。如果它有第二个参数，模板中就必须传进去**。

### 内置过滤器 Builtin Filters

Jinja2模板引擎提供了丰富的内置过滤器。这里介绍几个常用的。

#### 字符串操作

```python
{# 当变量未定义时，显示默认字符串，可以缩写为d #}
<p>{{ name | default('No name', true) }}</p>

{# 单词首字母大写 #}
<p>{{ 'hello' | capitalize }}</p>

{# 单词全小写 #}
<p>{{ 'XML' | lower }}</p>

{# 去除字符串前后的空白字符 #}
<p>{{ '  hello  ' | trim }}</p>

{# 字符串反转，返回"olleh" #}
<p>{{ 'hello' | reverse }}</p>

{# 格式化输出，返回"Number is 2" #}
<p>{{ '%s is %d' | format("Number", 2) }}</p>

{# 关闭HTML自动转义 #}
<p>{{ '<em>name</em>' | safe }}</p>

{% autoescape false %}
{# HTML转义，即使autoescape关了也转义，可以缩写为e #}
<p>{{ '<em>name</em>' | escape }}</p>
{% endautoescape %}
```

#### 数值操作

```python
{# 四舍五入取整，返回13.0 #}
<p>{{ 12.8888 | round }}</p>

{# 向下截取到小数点后2位，返回12.88 #}
<p>{{ 12.8888 | round(2, 'floor') }}</p>

{# 绝对值，返回12 #}
<p>{{ -12 | abs }}</p>
```

#### 列表操作

```python
{# 取第一个元素 #}
<p>{{ [1,2,3,4,5] | first }}</p>

{# 取最后一个元素 #}
<p>{{ [1,2,3,4,5] | last }}</p>

{# 返回列表长度，可以写为count #}
<p>{{ [1,2,3,4,5] | length }}</p>

{# 列表求和 #}
<p>{{ [1,2,3,4,5] | sum }}</p>

{# 列表排序，默认为升序 #}
<p>{{ [3,2,1,5,4] | sort }}</p>

{# 合并为字符串，返回"1 | 2 | 3 | 4 | 5" #}
<p>{{ [1,2,3,4,5] | join(' | ') }}</p>

{# 列表中所有元素都全大写。这里可以用upper,lower，但capitalize无效 #}
<p>{{ ['tom','bob','ada'] | upper }}</p>
```

#### 字典列表操作

```python
{% set users=[{'name':'Tom','gender':'M','age':20},
              {'name':'John','gender':'M','age':18},
              {'name':'Mary','gender':'F','age':24},
              {'name':'Bob','gender':'M','age':31},
              {'name':'Lisa','gender':'F','age':19}]
%}


{# 按指定字段排序，这里设reverse为true使其按降序排 #}
<ul>
{% for user in users | sort(attribute='age', reverse=true) %}
     <li>{{ user.name }}, {{ user.age }}</li>
{% endfor %}
</ul>

{# 列表分组，每组是一个子列表，组名就是分组项的值 #}
<ul>
{% for group in users|groupby('gender') %}
    <li>{{ group.grouper }}<ul>
    {% for user in group.list %}
        <li>{{ user.name }}</li>
    {% endfor %}</ul></li>
{% endfor %}
</ul>

{# 取字典中的某一项组成列表，再将其连接起来 #}
<p>{{ users | map(attribute='name') | join(', ') }}</p>
```

更全的内置过滤器介绍可以从[Jinja2的官方文档](http://jinja.pocoo.org/docs/dev/templates/#builtin-filters)中找到。

### Flask内置过滤器

Flask提供了一个内置过滤器`tojson`，它的作用是将变量输出为`JSON`字符串。这个在配合`Javascript`使用时非常有用。我们延用上节字典列表操作中定义的”users”变量

```html
<script type="text/javascript">
    var users = {{ users | tojson | safe }};
    console.log(users[0].name);
</script>
```

注意，这里要避免`HTML`自动转义，所以加上`safe`过滤器。

[day3完整demo代码下载](download/day3-demo.zip)