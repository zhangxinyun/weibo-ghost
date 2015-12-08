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
  
