---
title: 如何同时设置子域名和顶级域名到Github Pages
date: 2020-10-04 09:09:03
updated: 2020-10-04 09:09:03
tags:
	- Github
	- DNS
categories: 
	- Web
description: 目标：1) 通过Github Pages搭建自己的静态网站.  2)将自己购买的域名解析到Github Pages.  3) 将顶级域名example.com和子域名www.example.com解析到Github Pages。
cover: https://cdn.jsdelivr.net/gh/meixuhong/cdn@master/img-hosting/github_pages.jpeg
---


> 目标：1) 通过Github Pages搭建自己的静态网站.  2)将自己购买的域名解析到Github Pages.  3) 将顶级域名`example.com`和子域名`www.example.com`解析到Github Pages。



### 前置条件 

1. 在[Namesilo](https://www.namesilo.com/**?rid=8dbc698fz**)上购买域名`example.com`
2. 在Github搭建好Pages，参考[使用Hexo搭建Github Page](https://lmbiji.com/create-github-pages-with-hexo.html)
3. 已注册[cloudflare](https://www.cloudflare.com/)账号



### 主要步骤

1. **获取NS服务器** - 在[cloudflare](https://www.cloudflare.com/)上添加站点`example.com`，生成NS服务器域名
2. **配置NS服务器** - 在[Namesilo](https://www.namesilo.com/**?rid=8dbc698fz**)上将域名的NS服务器换成[cloudflare](https://www.cloudflare.com/)上的NS服务器
3. **DNS解析** - 在[cloudflare](https://www.cloudflare.com/)上设置DNS解析，包含`A`解析和`CNAME`解析
4. **设置Github Page的CNAME** - 在`Hexo`工程中的`source`下面添加CNAME文件，并在Github工程中设置绑定域名为顶级域名`example.com`



### 图解详细步骤



1. 在[cloudflare](https://www.cloudflare.com/)上添加站点，生成NS服务器域名。

![cloudflare添加站点](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/Cloudflare-addsite.jpg)

图中的`jonah.ns.cloudflare.com`与`stevie.ns.cloudflare.com`就是[cloudflare](https://www.cloudflare.com/)的NS服务器，NS服务器就是DNS服务器，是对域名进行DNS解析的服务器，国内最大的DNS服务器是`DNSPOD`，但是由于国内域名需要备案，只能解析到国外服务器IP，且`CNAME`解析可能有不可预知的问题。这也是我在尝试几次失败之后到[Namesilo](https://www.namesilo.com/**?rid=8dbc698fz**)上购买域名，到[cloudflare](https://www.cloudflare.com/)上解析DNS的原因。



2. 在[Namesilo](https://www.namesilo.com/**?rid=8dbc698fz**)上将域名的NS服务器换成[cloudflare](https://www.cloudflare.com/)上的NS服务器

选中指定域名右侧的DNS NS服务器，修改NS服务器为上述域名后提交，大概半小时可以生效，慢的话可能需要1天。

![](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/namesilo-dns-NS.jpg)



![](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/namesilo-dns-NS-change.jpg)



3. 在[cloudflare](https://www.cloudflare.com/)上设置DNS解析，包含`A`解析和`CNAME`解析



```bash
@        A        185.199.108.153
@        A        185.199.109.153
@        A        185.199.110.153
@        A        185.199.111.153
www      CNAME    your_github_username.github.io.
```

如何得知上述的4个IP地址呢？到 https://www.ipaddress.com/dns-lookup 中查询DNS即可。上表中的`your_github_username`需要换成自己的账号。解析大概需要1个小时左右生效。

![](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/cloudflare-lmbiji.com.jpg)





4.  在`Hexo`工程中的`source`下面添加CNAME文件，并在Github工程中设置绑定域名为顶级域名`example.com`

- 在工程文件的source目录下新建CNAME，写入顶级域名`lmbiji.com`, 使用`hexo clean && hexo g && hexo d`命令会在`public`目录下生成`CNAME`文件并上传到Github io对应的仓库下
- 在Github Pages选项中设置绑定顶级域名`lmbiji.com`

![](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/github-naked-domain.jpg)
