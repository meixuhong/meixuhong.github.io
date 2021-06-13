---
title: 【保姆式教程】搭建一套高速的永久免费CDN图床
date: 2021-06-13 08:01:41
updated: 2021-06-13 08:01:41
description: 通过PicX调用Github API,让Github免费成为永久免费图床，jsDelivr提供永久免费CDN加速，Vercel/Netlify为你提供免费图床网站托管.
categories: 
	- Web
tags:
	- Web
	- Tools
	- jsDelivr
	- Vercel
	- Netlify
cover: https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/wechat_gh_20210613.png
---

> 感谢大佬[XPoet](https://xpoet.cn/)开发的基于 GitHub API 开发的图床神器`picx`，感谢[jsDelivr](https://www.jsdelivr.com/)提供免费CDN 加速。

简单总结一下思路：

1. 到[github](https://github.com/meixuhong/picx)上克隆`picx`源码
2. 在[travis-ci](https://travis-ci.com/)上关联该`picx`项目
3. 在`vue2-dev`分支调测并推送静态网站源码至`gh-pages`分支
4. 在[Vercel](https://vercel.com)或者[Netlify](https://www.netlify.com/)上关联`gh-pages`部署为静态网页

## 从Github上克隆源码

登录到[github](https://github.com/meixuhong/picx)上克隆`picx`源码，其中`vue2-dev`分支是源码分支，`gh-pages`是用来存放静态网站的分支。

![github_picx](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/1-clone-picx-source.png)

为了能通过[travis-ci](https://travis-ci.com/)自动编译，我们需要对[github](https://github.com/meixuhong/picx)设置钩子。到[github setting](https://github.com/settings/tokens)上创建`token`，并关联至[travis-ci](https://travis-ci.com/).

![2-github-token-gen](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/2-github-token-gen.png)

创建一个新的`token`，设置`scope`含`repo`.

![3-github-token-scope](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/3-github-token-scope.png)

创建完成后，复制该`token`，需要注意的是该`token`只会出现一次，后续无法在`github`上查看，如果丢失，只能重新创建一个新的`token`，所以我们需要自己保存记录到本地。

## 在Travis-CI上关联该项目

在[travis-ci](https://travis-ci.com/)上关联该`picx`项目，如果没有`travis-ci`账号，可以使用`github`账号关联创建，此处不再复述。在`travis-ci`中设置环境变量，将刚才设置的`github`的`token`填入，如下图示。

- NAME填入`GH_TOKEN`
- VALUE填入`TOKEN值` , 即从github上创建生成的值
- BRANCH填入源码分支`vue2.x-dev`

![4-travis-ci-setting-for-picx](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/4-travis-ci-setting-for-picx.png.png)

## 编译生成静态网站

[travis-ci](https://travis-ci.com/)配置完成后，可以到`vue2-dev`源码分支修改文件，测试`travis-ci`是否支持编译了。比如，修改一下`Readme.md`文件并提交到仓库，`github`发生变化后，`travis-ci`通过钩子发现分支变化，于是开始编译，下图表示`travis-ci`正在编译`vue2.x-dev`分支源码。

![5-travis-building-project](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/5-travis-building-project.png)

黄色表示正在编译，不出意外会完成编译，最终是绿色。

![6-travis-ci-done](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/6-travis-ci-done.png)

完成编译后分别到github查看对应的源码状态。可以看到`vue2.x-dev`分支提交了一个文件。

![7-vue2](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/7-vue2.x-dev-branch-update.png)

`gh-pages`分支则由**travisbot**完成了编译。

![8-gh-pages-branch-update](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/8-gh-pages-branch-update.png)

至于如何在该分支编译的，咱们暂且不用关注，如果感兴趣，可以查看一下`vue2.x-dev`分支下的`.travis.yml`源码。

```yml
# 编译语言、环境
dist: xenial
os: linux
language: node_js

# Node.js 版本
node_js:
  - 12

cache: npm

# 只有 源码 分支更改才触发 CI
branches:
  only:
    - vue2.x-dev

before_install:
  - export TZ='Asia/Shanghai'

install:
  - npm install # 安装依赖

script:
  - npm run build # 执行打包命令，生成 dist 静态文件

deploy:
  strategy: git
  provider: pages
  skip_cleanup: true      # 跳过清理
  token: $GH_TOKEN        # GitHub Token 变量
  keep_history: true      # 保持推送记录，以增量提交的方式
  local_dir: dist         # 需要推送到 GitHub 的静态文件目录
  target_branch: gh-pages # 推送的目标文件 local_dir -> gh-pages 分支
  on:
    branch: vue2.x-dev        # 源码工作分支
```

## Vercel托管静态网站

[Vercel](https://vercel.com/)为开发者提供免费的一键式托管服务，可以通过导入主流的代码托管平台的项目来进行静态网站托管。选择 Vercel 的原因不仅是因为其完全免费，而且在国内环境下，其部署的网站访问速度也算是一流。

> [Netlify](https://www.netlify.com/)也提供相同的功能与类似的CDN全站加速功能，两者功能与用法也都差不多，可以二选一。

如果没有vercel账号，可以绑定github账号快速注册，完成注册后可以直接导入对应工程，如下图示。

![9-vercel-import-project](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/9-vercel-import-project.png)

导入工程示意图如下：

![10-Select-vercel-scope](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/10-Select-vercel-scope.png)

![11-import-default-branch-to-vercel](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/11-import-default-branch-to-vercel.png)

![12-import-default-branch-to-vercel_build-options](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/12-import-default-branch-to-vercel_build-options.png)

![13-start-building-project-in-vercel](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/13-start-building-project-in-vercel.png)

![14-build-done-in-vercel](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/14-build-done-in-vercel.png)

完成部署后，可点击**Visit**直接访问，填入之前配置的`github token`即可直接使用。填入token后可以选择github上的一个仓库，作为图床base，图片都存放于此，下面示意为，选择[cdn](https://github.com/imlaomei/cdn)仓库。

![16-cdn-img-hosting-setting](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/16-cdn-img-hosting-setting.png)

配置完成之后，就可以通过web直接上传图片了，当然也可以通过PicGo等工具设置自动上传。

![17-cdn-img-hosting-overview](https://cdn.jsdelivr.net/gh/imlaomei/cdn@main/img-hosting/17-cdn-img-hosting-overview.png)

> 后记：如果有域名，可以在Vercel上加一个自己的域名，不再复述，以上。