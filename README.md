# weibo-ghost
使用 Goast.py 访问新浪微博

## 运行环境

Ubuntu 12.04 with Python 2.7

安装构建依赖包

    apt-get install python-dev build-essential
    
安装 Xvfb

    apt-get install xvfb

安装 pip

    wget https://bootstrap.pypa.io/get-pip.py
    python get-pip.py

安装 SIP

下载地址：<https://www.riverbankcomputing.com/software/sip/download>

    wget http://sourceforge.net/projects/pyqt/files/sip/sip-<version>/sip-<version>.tar.gz
    tar -xvf sip-<version>.tar.gz
    cd sip-<version>
    python configure.py
    make
    make install

安装 PyQt4

下载地址：<https://riverbankcomputing.com/software/pyqt/download>

    wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-<version>/PyQt-x11-gpl-<version>.tar.gz
    tar -xvf PyQt-x11-gpl-<version>.tar.gz
    cd PyQt-x11-gpl-<version>
    python configure.py
    make
    make install

安装 Ghost.py

    pip install ghost.py --pre
  
## 使用说明

导入 *Weibo* 类，并实例化：

    from weibo import Weibo
    wb = Weibo()

### 用户登录

编辑 *conf.yml* 文件，输入新浪微博账号和密码：

    username: AnthonyLi
    password: secret

执行 login 方法：

    wb.login()

登录成功后，会在项目根目录下生成一个 cookies 文件

### 搜索

TODO
