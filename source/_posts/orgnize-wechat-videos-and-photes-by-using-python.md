---
title: 使用Python实现快速整理微信视频与照片
date: 2016-09-18 18:24:57
categories: python
description: 作为超级APP，微信已经成了移动互联网的入口。而我们也早已习惯通过微信收发图片与视频等多媒体文件。身为一名屌丝通信狗，经常出差海外，跟家人的沟通方式主要就靠微信了，每当累了或抑郁了，打开微信看看家人的视频照片，就觉得开心多了。最终，微信变得越来越臃肿，视频与图片也必须早点保存到手机或者电脑。但是最终导出的文件命名是让人相当崩溃的。有没有办法快速重新命名呢？
tags: 
    - Python
    - 微信
---

作为超级APP，微信已经成了移动互联网的入口。而我们也早已习惯通过微信收发图片与视频等多媒体文件。身为一名屌丝通信狗，经常出差海外，跟家人的沟通方式主要就靠微信了，每当累了或抑郁了，打开微信看看家人的视频照片，就觉得开心多了。最终，微信变得越来越臃肿，视频与图片也必须早点保存到手机或者电脑。但是最终导出的文件命名是让人相当崩溃的。有没有办法快速重新命名呢？

![wechat1](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/Wechat-photoes-vedios-orgnize.jpg)



## 使用自动化利器Python
作为批量处理文件的利器，当然非Python莫属了，而且有一堆优质库可供调用，基本搜索一下能解决90%需求。对于这个需求初始想法是直接通过os库获取文件的创始时间，依此来重新命名文件，可是最终发现os库获取的是文件第一次拷贝到系统的时间，并非文件的初始创建时间。比如，2016-09-10日19：00：23拷贝2016-06-16日10：00：00拍摄的视频文件到系统硬盘，系统就记录其时间为2016-09-10日19：00：23，并非6月16日。
上网搜了很久，发现使用exif与ffmpeg可以分别对照片与视频提取初始创建时间：

### exif工具
[Exif是用来存储数码照片的属性信息与拍摄数据的，可以附加于JPEG、TIFF、RIFF等文件之中，为其增加有关数码相机拍摄信息的内容和索引图或图像处理软件的版本信息](https://zh.wikipedia.org/wiki/EXIF)。

使用exif工具查询当前目录下的pic1.png文件可以得到如下信息：
`MacBook:BaiduYun meixuhong$ exif -i pic1.png`

```Python
EXIF tags in 'pic1.png' ('Motorola' byte order):
------+------------------------------------------------------------------------
Tag   |Value
------+------------------------------------------------------------------------
0x010f|Apple
0x0110|iPhone 6s
0x0112|Right-top
0x011a|72
0x011b|72
0x0128|Inch
0x0131|9.2.1
0x0132|2016:03:08 21:22:46
```
显然获取到照片拍摄时间为2016:03:08 21:22:46。

### ffmpeg工具
ffmpeg自然不用多说，一款开源的牛逼哄哄的绝大多数开发者与公司都在用的音频解码软件。使用它解析视频文件自然也不在话下。如使用它解析1.mov文件，则会输出如下信息：
`MacBook:BaiduYun meixuhong$ ffmpeg -i 1.mov`

```Python
ffmpeg version 3.1.3 Copyright (c) 2000-2016 the FFmpeg developers
#略去若干字
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '1.mov':
  Metadata:
    major_brand     : qt  
    minor_version   : 0
    compatible_brands: qt  
    creation_time   : 2016-07-10 09:36:54
    com.apple.quicktime.location.ISO6709: +30.2216+115.9852-244.943/
    com.apple.quicktime.make: Apple
    com.apple.quicktime.model: iPhone 6s
    com.apple.quicktime.software: 9.3.2
    com.apple.quicktime.creationdate: 2016-07-10T17:36:54+0800
  Duration: 00:01:05.95, start: 0.000000, bitrate: 8559 kb/s
#略去若干字
```
获取到视频文件拍摄于2016-07-10 09:36:54。

这俩工具当然无懈可击，可是要想用python解析的话就得使用进程调用它们，而且只能将输出结果保存在文本中，那如果有300个文件就得要输出300个文本文件，很复杂，显然不是我要的结果，需要换思路。

### 杀鸡焉用牛刀 - 小巧的Hachoir
[Hachoir is a Python library to view and edit a binary stream field by field. In other words, Hachoir allows you to “browse” any binary stream just like you browse directories and files.](https://pypi.python.org/pypi/hachoir3-superdesk/3.0a1.post2)
即是说使用Hachoir可以直接查看文件的二进制文件，提取文件的[metadata](https://en.wikipedia.org/wiki/Metadata)即可获取到数码照片与视频的初始创建时间了。

实现过程到还是到我的项目主页[Github](https://github.com/wowmarcomei/RenameVideosImages)一览吧。

![wechat2](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/Wechat-orgnize-demo.gif)

执行完Python脚本，再来看各个文件名，感觉整个世界瞬间变得美好了。

![wechat3](https://cdn.jsdelivr.net/gh/meixuhong/cdn/img/Wechat-photoes-vedios-orgnize-result.jpg)
