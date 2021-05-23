---
title: WSL Ubuntu 18.04上使用pipenv的4个关键点
date: 2021-05-03 08:01:41
updated: 2021-05-03 08:01:41
description: 自从MicroSoft拥抱Linux以来，除了微软股票大涨以外，其开源动作更是不断，VScode俨然已成为最流行的开源IDE/文本编辑器，WSL更像是王炸，从此大家再也不需要安装双系统了吧。本文简要总结安装WSL Ubuntu 18.04后，pipenv的基本使用笔记。
categories: 
	- Python
tags:
	- WSL
	- Python
cover: https://cdn.jsdelivr.net/gh/meixuhong/cdn@master/img-hosting/linux-windows.png
---

> 自从MicroSoft拥抱Linux以来，除了微软股票大涨以外，其开源动作更是不断，VScode俨然已成为最流行的开源IDE/文本编辑器，WSL更像是王炸，从此大家再也不需要安装双系统了吧。本文简要总结安装WSL Ubuntu 18.04后，pipenv的基本使用笔记。

## 1.Pipenv的常见命令

```shell
pipenv install  # 安装虚拟环境 ，如果工程目录下有Pipfile则会自动安装，如果没有则会先生成Pipfile
pipenv shell    # 进入虚拟环境
exit            # 退出虚拟环境
pipenv --rm     # 删除整个环境  不会删除pipfile
pipenv -h 	    # 查看帮助
pipenv install requests==2.13.0 #安装指定版本包
```

## 2.以root账号执行profile使环境变量生效

使用WSL基本都是没有使用`bash --login`的，这就导致基本环境变量没有加载，需要我们手动加载使环境变量生效。

```shell
$ sudo -s
# source ~/.profile
```

否则会出现找不到`pipenv`,参考自[superuser](https://superuser.com/questions/1432768/how-to-properly-install-pipenv-on-wsl-ubuntu-18-04)。

## 3.修改项目的Pipfile中的url为国内镜像地址

```shell
[[source]]
name = "pypi"
url = "https://repo.huaweicloud.com/repository/pypi/simple"
verify_ssl = true

[dev-packages]

[packages]

[requires]
python_version = "3.6"
```

url可以修改为华为镜像https://repo.huaweicloud.com/repository/pypi/simple，或者阿里镜像https://mirrors.aliyun.com/pypi/simple。

或者，在环境变量中指定源，这样可以一劳永逸的解决镜像问题。

在`用户环境变量文件(~/.bash_profile，或者~/.profile)`或者`系统环境变量文件(/etc/profile)`中添加都行。

```shell
export PIPENV_TEST_INDEX=https://repo.huaweicloud.com/repository/pypi/simple
export PATH=$PIPENV_TEST_INDEX:$PATH
```

编辑完成之后，执行`source ~/.profile`生效环境变量。

## 4.修改Pipenv的虚拟环境的默认生成目录

共有三种方法：

1. `export PIPENV_VENV_IN_PROJECT=1` 设置这个环境变量，pipenv会在当前目录下创建.venv的目录，以后都会把模块装到这个.venv下。
2. 自己在项目目录下手动创建.venv的目录，然后运行 `pipenv run` 或者 `pipenv shell `pipenv都会在.venv下创建虚拟环境。
3. 设置`WORKON_HOME`到其他的地方 （**如果当前目录下已经有.venv,此项设置失效**）

我喜欢通过设置`WORKON_HOME`到指定目录，在`~/.profile`下增加环境变量：

```shell
export WORKON_HOME=/home/laomei/pipenv_home
export PATH=$WORKON_HOME:$PATH
```

然后生效环境变量`source ~/.profile`即可。

