这里有两个分支：
- master: 存放github page的静态网站，使用hexo命令维持博客更新。
- hexo：源代码原始文件，通过hexo命令生成public目录会被推送到master分支，使用原始git命令维持版本更新。

public目录内容如下：

```shell
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 2016/
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 2017/
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 about/
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 archives/
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 categories/
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 css/
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 images/
-rw-r--r-- 1 meixuhong 1049089 34298 7月  15 17:58 index.html
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 js/
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 lib/
-rw-r--r-- 1 meixuhong 1049089   187 7月  15 17:58 README.md
-rw-r--r-- 1 meixuhong 1049089 29141 7月  15 17:58 search.xml
drwxr-xr-x 1 meixuhong 1049089     0 7月  15 17:58 tags/
```

使用如下命令，将Hexo目录下的public目录发布上传到master分支发布，每次需要推写文章时执行该命令即可。
> $ hexo clean && hexo g && gulp && hexo d


