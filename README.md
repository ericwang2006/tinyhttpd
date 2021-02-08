# 简介
tinyhttpd是一个非常轻量级的http服务器，只有500多行代码，编译后只有20多K，适用于某些对程序体积要求比较苛刻的场合，甚至还支持CGI，我在htdocs下加了一个shell.cgi的例子，可以只用shell脚本写CGI代码（可以省去perl）


# 原始源码地址
https://sourceforge.net/projects/tinyhttpd/

# 修改说明
- 这个项目并不能直接在Linux上编译运行，它本来是在solaris上实现的。
- 我按照[这篇](https://www.cnblogs.com/qiyeboy/p/6296387.html)文章的介绍进行了修改，[这里](https://github.com/qiyeboy/SourceAnalysis)也有文章作者修改的代码并有代码分析
- 我增加了一个--port参数，可以指定监听的端口

# 编译方法

```
git clone git@github.com:ericwang2006/tinyhttpd.git
cd tinyhttpd
make httpd
```
# 注意事项
- 网站文件存放在htdocs目录下，默认主页index.html
- 如果是静态文件不能带执行权限
- 如果是cgi文件必须带执行权限
