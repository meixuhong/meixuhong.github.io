---
title: Flask系列学习笔记
date: 2020-10-24 20:00:51
categories: 
  - Flask
description: Flask系列学习笔记-Day1. 写给自己看的笔记，学到哪里记到哪里？
tags: 
  - flask
---

# 1. 准备工作

Flask是基于Python的web应用框架，部署一个Flask应用依赖：

1. Python3应用
2. pipenv：生成虚拟化的环境，避免各个包相互影响依赖
3. Flask库，可以通过pip安装

```bash
$ python3 --version
Python 3.6.9
$ pip --version
pip 20.2.2 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
$ ls /mnt/d/Project/Flask_day1/
Pipfile   Pipfile.lock   demo.py
```

>**pipenv使用方式：**
>
>- 在指定工程目录使用`pipenv install`即可

