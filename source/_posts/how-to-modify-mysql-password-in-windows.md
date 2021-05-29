---
title: Windows下修改Mysql密码
date: 2018-07-21 11:27:51
updated: 2018-07-21 11:27:51
categories: 
	- SQL
	
description: 之前在Windows上装过一次Mysql学习，后来由于电脑原因卸载了，这次重新安装后，发现在配置过程中失败，退出配置后直接登录也不行，多次查询之后才知道原来是因为很久之前安装的mysql的密码与这次安装的密码不一致导致的，可是，过了这么久天知道我当时设置的啥密码啊。。。好吧，那就重置吧。
tags:
    - Mysql
cover: https://cdn.jsdelivr.net/gh/meixuhong/cdn@master/img-hosting/mysql.png    
---

之前在Windows上装过一次Mysql学习，后来由于电脑原因卸载了，这次重新安装后，发现在配置过程中失败，退出配置后直接登录也不行，多次查询之后才知道原来是因为很久之前安装的mysql的密码与这次安装的密码不一致导致的，可是，过了这么久天知道我当时设置的啥密码啊。。。好吧，那就重置吧。

- 环境： Windows 10
- Mysql 版本： mysql community 5.7.21.0
- CMD： 系统自带cmd，管理员权限

## 1. 重置步骤

### 1.1 停止mysql服务

使用管理员权限cmd执行下面命令停止服务

```powershell
# net stop mysql57
```

### 1.2 配置mysql跳过安全检查

```powershell
#cmd 1:
#my.ini为配置文件
mysqld --defaults-file="C:\ProgramData\MySQL\MySQL Server 5.7\my.ini" --console --skip-grant-tables
```

### 1.3 重置密码

```powershell
#cmd 2: 使用管理员权限打开另外一个cmd窗口，由于上面的cmd1窗口在运行着，所以我们可以不用输入密码进行登录
>mysql -u root
#修改mysql数据库中的表user，给user表中的root账号修改密码
$mysql> use mysql;
#注意新版本需要使用authentication_string修改密码
$mysql> update user set authentication_string=password("abcdefg123") where user='root';
#刷新表
$mysql> flush privileges;
```

### 1.4 关闭mysqld进程

关闭两个cmd窗口，Ctrl+Shift+Esc打开任务管理器找到mysqld的进程，将其杀死。

### 1.5 重新启动mysql服务： 

打开计算管理——>服务与应用程序—->服务—>mysql，启动服务。

### 1.6 登录mysql

```powershell
#执行下面命令，输入密码即可登录
> mysql -u root -p
```
