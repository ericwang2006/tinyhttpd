# 简介
tinyhttpd是一个非常轻量级的http服务器，只有500多行代码，编译后只有20多K，适用于某些对程序体积要求比较苛刻的场合，甚至还支持CGI，我在htdocs下加了一个shell.cgi的例子，可以只用shell脚本写CGI代码（可以省去perl）


# 原始源码地址
https://sourceforge.net/projects/tinyhttpd/

# 修改说明
- 这个项目并不能直接在Linux上编译运行，它本来是在solaris上实现的。
- 我按照[这篇](https://www.cnblogs.com/qiyeboy/p/6296387.html)文章的介绍进行了修改，[这里](https://github.com/qiyeboy/SourceAnalysis)也有文章作者修改的代码并有代码分析
- 我增加了一个--port参数，可以指定监听的端口，例如 `httpd --port 8080`

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

* * *

# Introduction
tinyhttpd is a very lightweight http server, with only more than 500 lines of code, and only more than 20K after compilation. It is suitable for some occasions where the program size is more demanding. It even supports CGI. I added a shell under htdocs. .cgi example, you can write CGI code only with shell script (perl can be omitted)

# Original source url
https://sourceforge.net/projects/tinyhttpd/

# Modify the description
This project cannot be compiled and run directly on Linux, it was originally implemented on solaris.
I modified it according to the introduction of [this article](https://www.cnblogs.com/qiyeboy/p/6296387.html), and [here](https://github.com/qiyeboy/SourceAnalysis) is also the code modified by the author of the article and a code analysis
I added a --port parameter, you can specify the listening port，
For example `httpd --port 8080`

# Compilation
```
git clone git@github.com:ericwang2006/tinyhttpd.git
cd tinyhttpd
make httpd
```
# Precautions
- The website files are stored in the htdocs directory, the default homepage index.html
- If it is a static file, it cannot have execute permission
- If it is a cgi file, it must have execute permission
