---
title: 使用Hexo搭建Github Page
date: 2016-07-06 15:37:51
updated: 2018-08-13 11:05:44
categories: 
  - Web
description: 在github上可以用户名创建一个repository,该仓库即为一个静态页面github page，可以在github上该仓库的设置界面选择主题来设置自己喜欢的主题，也可以通过`Hexo`来更新整个github page。为了可以在多台电脑上均可管理hexo源码与发布github page博客博文，我们需要使用两个分支：`master` 与 `hexo`。
tags: 
  - Hexo
  - Github
  - Git
cover: https://cdn.jsdelivr.net/gh/meixuhong/cdn@master/img-hosting/hexo-cover.png
---

> Github Pages是Github免费提供的静态网站服务，我们可以将自己的静态网站推送到Github仓库，让它提供网站服务，**免去自己申请主机服务器的困(费)扰(用)**。不过默认对外提供的域名为`<username>.github.io`，如果希望使用自己的域名如`baidu.com`，则需要对该域名进行`CNAME`解析到`<username>.github.io`.


在github上可以用户名创建一个repository: `<username>.github.io`，该仓库即为一个静态页面github page，可以在github上该仓库的设置界面选择主题来设置自己喜欢的`theme`，也可以通过`Hexo`来更新整个github page。为了可以在多台电脑上**均可**管理hexo源码与发布github page博客博文，我们需要使用两个分支：`master` 与 `hexo`。

- hexo分支为源代码文件。
- master分支为发布的github page静态页面所需的所有文件，设置为默认分支。


```bash
$cd
$wget https://nodejs.org/dist/v10.15.3/node-v10.15.3-linux-x64.tar.gz
$tar -xzvf node-v10.15.3-linux-x64.tar.gz
$mv node-v10.15.3-linux-x64 nodejs
```

配置环境变量使nodejs与npm生效。以ubuntu16.04环境为例。

```bash
vi .profile  
# 在PATH中添加nodejs所在位置路径，其中冒号:表示一个路径的结束，$HOME/nodejs/bin为新加的路径
PATH="$HOME/bin:$HOME/.local/bin:$PATH:$HOME/nodejs/bin"

# 执行source .profile或者reboot系统之后环境变量生效
source .profile

$ node --version
v10.15.3
$ npm --version
6.4.1
$
```

### 2. 在本地搭建hexo环境

在环境变量生效以后，普通账号拥有nodejs与npm程序，使用普通账号基于全局安装hexo

```bash
$ npm install -g hexo-cli
```

配置ssh密钥，加入到github中,可以参考[官方指导Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

### 3. 在本地搭建master分支

1. 在github上创建仓库：`wowmarcomei.github.io`，默认分支为`master`.
2. 添加README.md到**master**分支
3. 创建**hexo**分支
4. 在本地clone hexo分支

```bash
$ git clone -b hexo git@github.com:wowmarcomei/wowmarcomei.github.io.git
$ cd wowmarcomei.github.io.git
$ hexo init
```

在空仓库中初始化hexo工程，生成会生成hexo的工程文件，包括package.json等如下文件。

```bash
   drwxrwxr-x   6 ubuntu ubuntu   4096 Apr  1 11:10 ./
   drwxr-xr-x  10 ubuntu ubuntu   4096 Apr  1 11:10 ../
   -rw-rw-r--   1 ubuntu ubuntu   1765 Apr  1 11:10 _config.yml
   -rw-rw-r--   1 ubuntu ubuntu     65 Apr  1 11:10 .gitignore
   drwxrwxr-x 284 ubuntu ubuntu  12288 Apr  1 11:10 node_modules/
   -rw-rw-r--   1 ubuntu ubuntu    443 Apr  1 11:10 package.json
   -rw-rw-r--   1 ubuntu ubuntu 137375 Apr  1 11:10 package-lock.json
   drwxrwxr-x   2 ubuntu ubuntu   4096 Apr  1 11:10 scaffolds/
   drwxrwxr-x   3 ubuntu ubuntu   4096 Apr  1 11:10 source/
   drwxrwxr-x   3 ubuntu ubuntu   4096 Apr  1 11:10 themes/
```

其中node_modules文件是每个nodejs工程所需要安装的依赖包，不是全局包，每个工程都应该有一个这样目录，但是上传到github时最好把它删除掉，新用户clone该仓库后，可以在目录下执行`npm install`命令来生成新的node_modules目录。

_config.yml是网站的配置文件，包括主题选择等等。需要修改该文件指定托管部署地址。

```yaml
$ vi _config.yml

# Deployment
## Docs: https://hexo.io/docs/deployment.html
deploy:
  type: git
  repo: git@github.com:wowmarcomei/wowmarcomei.github.io.git
  branch: master
```

设置主题，可以选择**hexo-theme-even**主题，参考[github](<https://github.com/ahonn/hexo-theme-even>)主页提示执行如下步骤安装。

```bash
$ cd wowmarcomei.github.io.git
$ npm install hexo-renderer-scss --save
$ git clone https://github.com/ahonn/hexo-theme-even themes/even
```

下载好了主题以后，修改配置文件中的 `theme` 字段为 `even`:

```shell
# Extensions
# Plugins: http://hexo.io/plugins/
# Themes: http://hexo.io/themes/
theme: even
```

更多主题设置，查看 [Document](https://github.com/ahonn/hexo-theme-even/wiki), 可以删除themes主题下的`.git`目录与`.gitignore`文件。

如果使用的是[snippet](<https://github.com/shenliyang/hexo-theme-snippet>)主题，因为 **hexo-theme-snippet** 使用了 `ejs` 模版引擎 、 `Less` CSS预编译语言以及在官方插件的基础上 进行功能的开发，以下为必装插件：

```bash
npm install hexo-renderer-ejs hexo-renderer-less hexo-deployer-git -S
```

在通过git上传到github之前，需要安装`hexo-deployer-git`，可以全局安装，也可以本地工程安装。下面采取本地安装。

```bash
npm install --save hexo-deployer-git
```

还有一些可选的hexo插件，可以安装到本地工程目录中去：

```bash
npm install hexo-server --save
npm install hexo-admin --save
npm install hexo-generator-archive --save
npm install hexo-generator-feed --save
npm install hexo-generator-search --save
npm install hexo-generator-tag --save
npm install hexo-deployer-git --save
npm install hexo-generator-sitemap --save

npm install hexo-renderer-marked --save
npm install hexo-renderer-markdown-it --save

npm install hexo-symbols-count-time --save

npm install hexo-generator-sitemap --save #sitemap.xml适合提交给谷歌搜素引擎
npm install hexo-generator-baidu-sitemap --save #baidusitemap.xml适合提交百度搜索引擎

npm install gulp -g
npm install gulp-minify-css gulp-uglify gulp-htmlmin gulp-htmlclean gulp --save

npm install hexo-generator-searchdb --save
```

后续继续执行hexo命令来生成静态网站。

```bash
$ hexo clean
$ hexo g # 用hexo生成静态网站，位于public目录
$ hexo s # 本地生成查看静态网站，启动服务器业务
$ hexo d # 生成.deploy_git目录上传到托管网站github相应路径，即上传到master分支
```

   > 注：
   >
   > - `--save`参数会将库安装到本目录下的node_modules下面。
   > - nodejs工程将需要安装的包写在`package.json`文件中。
   > - 使用`npm audit -fix`可以查出工程还需要哪些包
   > - 可以到https://mirrors.huaweicloud.com/下面查看nodejs加速镜像


### 4. 在本地搭建hexo分支

上面已经在github上创建了hexo分支，使用git命令提交hexo程序到github的hexo分支。

```bash
$ git add *
$ git commit -m "Initial Hexo Branch"
$ git push origin hexo # 推送到hexo分支
```

## 二.在其他电脑搭建Hexo环境

> 该电脑可以做hexo源码重新开发也可以只用作发布blog，可以分别通过控制hexo与master分支来进行同步即可。

1. 搭建nodejs与npm环境，与上述步骤相同

2. 搭建hexo全局环境，与上述步骤相同

3. 生成ssh-key密钥，添加到github中，与上述步骤相同

4. 复制hexo分支代码到本机

```bash
$ git clone -b hexo git@github.com:wowmarcomei/wowmarcomei.github.io.git
$ cd wowmarcomei.github.io
$ git branch #查看当前分支，应该为hexo
$ rm -fr node_modules  #如果从github中clone下来的工程中有该目录就删除掉, 没有就算了
$ vim .gitignore #加入node_modules,public, .deploy_git这几个目录，
$ npm install #在工程目录中用 npm install 命令生成node_modules，每个项目有单独一套node_modules（像Java中的Maven那样),如果出现一些包需要更新的提示，如提示使用npm audit fix进行修复，则执行该命令
```

   如果使用的是[snippet](<https://github.com/shenliyang/hexo-theme-snippet>)主题，因为 **hexo-theme-snippet** 使用了 `ejs` 模版引擎 、 `Less` CSS预编译语言以及在官方插件的基础上 进行功能的开发，以下为必装插件：

```bash
npm install hexo-renderer-ejs hexo-renderer-less hexo-deployer-git -S
npm install hexo-generator-json-content@2.2.0 -S #本地站点搜索插件
```

   在通过git上传到github之前，需要安装`hexo-deployer-git`，可以全局安装，也可以本地工程安装。下面采取本地安装。

```bash
npm install --save hexo-deployer-git
```

   还有一些可选的hexo插件，可以安装到本地工程目录中去：

```bash
npm install hexo-server --save
npm install hexo-admin --save
npm install hexo-generator-archive --save
npm install hexo-generator-feed --save
npm install hexo-generator-search --save
npm install hexo-generator-tag --save
npm install hexo-deployer-git --save
npm install hexo-generator-sitemap --save
   
npm i hexo-renderer-marked --save
npm i hexo-renderer-markdown-it --save
   
npm install hexo-symbols-count-time --save
   
npm install hexo-generator-sitemap --save #sitemap.xml提交给谷歌引擎
npm install hexo-generator-baidu-sitemap --save #baidusitemap.xml适合提交百度搜索引擎
   
npm install gulp --save
npm install gulp-minify-css gulp-uglify gulp-htmlmin gulp-htmlclean gulp --save
   
npm install hexo-generator-searchdb --save
```

   

> 注：
>
> - `--save`参数会将库安装到本目录下的node_modules下面。
> - nodejs工程将需要安装的包写在`package.json`文件中。
> - 使用`npm audit -fix`可以查出工程还需要哪些包
> - 可以到https://mirrors.huaweicloud.com/下面查看nodejs加速镜像

   

5. 如果需要对Hexo源码进行操作,发布到hexo分支

```bash
$ git add *
$ git commit -m "your comment"
$ git push origin hexo #推送到远程github的hexo分支
```

6. 如果需要更新blog，则使用hexo操作发布到master

```bash
$ hexo clean
$ hexo g
$ gulp   #压缩html,css,js文件
$ hexo s #s为本地server模式
$ hexo d #d为deploy部署模式
```

> **如果有更换电脑，直接在新电脑上将hexo分支clone下来即可, master分支可以通过hexo命令生成** 。另外，如果需要定制主题的话，一般是在`header.ejs`与`style.css`下面定制头与css样式。