homepage
========

A blog written by django.


Start
=======

$ git clone https://github.com/xgfone/homepage
$ cd homepage/homepage
$ python manage.py syncdb   # 初始化数据库，会提示是否建立后台管理员账号，选择是，并输入账号和密码
$ python manage.py runserver

然后打开浏览器，输入 127.0.0.1:8000 并按回车键即可。
注：输入 127.0.0.1:8000/admin 可进入后台。
