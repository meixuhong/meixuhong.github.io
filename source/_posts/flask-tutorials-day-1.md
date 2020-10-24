---
title: Flask系列学习笔记
date: 2020-10-24 20:00:51
categories: 
  - flask
description: Flask系列学习笔记-Day1. 写给自己看的笔记，学到哪里记到哪里？
tags: 
  - flask
---

# # 准备工作

Flask是基于Python的web应用框架，部署一个Flask应用依赖：

1. 安装Python3应用

```bash
$ python3 --version
Python 3.6.9
$ pip --version
pip 20.2.2 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
```

2. pipenv：生成虚拟化的环境，避免各个包相互影响依赖

- 在指定工程目录使用`pipenv install`即可生成对应的虚拟环境，完成后在目录下生成`Pipfile`和`Pipfile.lock`文件。

```bash
$pipenv install
$ ls /mnt/d/Project/Flask_day1/
Pipfile   Pipfile.lock   demo.py
```

- 下次想要激活该虚拟环境的话，在该工程目录使用命令`pipenv shell`

```bash
$pipenv shell
```

- 如果在**VSCODE**中想调用该虚拟环境对应的`Python`，在工程目录下设置：**Ctrl-Shift-P**,选择`Python-Interpreter`为`/home/[username]/.local/share/virtualenvs/[xxxxx]/bin/python3`,则最终会在工程目录下生成`.vscode/settings.json`文件

```json
{
  "python.pythonPath": "/home/[username]/.local/share/virtualenvs/[xxxx]/bin/python3"
}
```

3. 安装Flask库，可以通过pip安装

```bash
meixuhong@meixuhong:/mnt/d/Project/Flask_day1$ pipenv shell
(Flask_day1) meixuhong@meixuhong:/mnt/d/Project/Flask_day1$ pip install flask
(Flask_day1) meixuhong@meixuhong:/mnt/d/Project/Flask_day1$ pip list
Package      Version
------------ -------
click        7.1.2
Flask        1.1.2
itsdangerous 1.1.0
Jinja2       2.11.2
MarkupSafe   1.1.1
pip          20.2.3
setuptools   50.3.0
Werkzeug     1.0.1
wheel        0.35.1
```

# # 4步开发Flask应用

可以通过4步快速开发一个flask应用：**导入Flask类 --> 初始化Flask实例 --> 设置路由函数(视图函数) --> 启动应用**.

1. 导入Flask类

```python
# 导入Flask类
from flask import Flask
```

2. 初始化Flask实例

```python
#Flask类接收一个参数__name__, __name__表示的是本文件名，如文件名为demo.py，则此处的__name__最终被赋值为demo.py
app = Flask(__name__)
```

3. 设置路由函数

```python
# 装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    return('Hello world!')
```

4. 启动应用

```python
# Flask应用程序实例的run方法启动WEB服务器,设置参数debug=True,则修改代码后可以不用重新启动服务器做调试
if __name__ == '__main__':
    app.run(debug=True)
```

![](https://cdn.jsdelivr.net/gh/meixuhong/cdn//img/day1-1.jpg)

[完整demo下载](/download/README.md)

# # 进阶

1. 动态url

很多时候url是动态变化的，这个时候可以通过变量传递，有两点注意事项：

- **路由的变量通过`<>`来指定，该变量对应为下面函数的变量，两者保持一致**
- 路由传递的参数默认当做`string`处理，也可以指定`int`，变量名在`:`后，即`type:variable`

```python
@app.route('/<string:name>/<int:id>')
def hello_user(name,id):
    return 'Hello {} {}'.format(name,id)
```

![](https://cdn.jsdelivr.net/gh/meixuhong/cdn//img/day1-2.jpg)

2. 通过Flask-Script模块，可以通过命令行的形式来操作Flask.