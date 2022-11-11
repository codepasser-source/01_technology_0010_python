## 运行环境

### 安装 `Python` 环境

#### 安装 `python3`

```shell
# 官网
https://www.python.org/
# 版本
3.8.0
# WINDOW
https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe
# MAC
https://www.python.org/ftp/python/3.8.0/python-3.8.0-macosx10.9.pkg

# 确认安装
# MAC系统自带的python2.7，目录为/usr/bin/python
which python
# brew安装的python3.8,目录为/usr/local/bin/python3
which python3
```

```shell
# 依赖
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

./configure --prefix=/usr/local/lib/python3
make && make install

alternatives --list
# 手动安装
alternatives --install /usr/bin/python3 python3 /usr/local/lib/python3/bin/python3 60
alternatives --config python3
alternatives --install /usr/bin/pip3 pip3 /usr/local/lib/python3/bin/pip3 60
alternatives --config pip3

alternatives --install /usr/bin/python python /usr/local/lib/python3/bin/python3 60
alternatives --config python
alternatives --install /usr/bin/pip pip /usr/local/lib/python3/bin/pip3 60
alternatives --config pip

alternatives --remove python3 /usr/local/lib/python3/bin/python3
alternatives --remove pip3 /usr/local/lib/python3/bin/pip3

alternatives --remove python /usr/local/lib/python3/bin/python3
alternatives --remove pip /usr/local/lib/python3/bin/pip3

# 配置yum 把 #! /usr/bin/python 修改为 #! /usr/bin/python2
vi /usr/bin/yum 
vi /usr/libexec/urlgrabber-ext-down 
vi /usr/bin/yum-config-manager
```

#### 安装 `pip`

```shell
# 安装Python2.7以上版本，会自动带pip。
# 系统自带的python没有pip，只有easy_install
# 给系统的python安装pip
easy_install pip
# 卸载 手动删除文件
easy_install -m pip

# Python3高版本自带pip3
pip3 -V

# 升级 pip
pip3 install --upgrade pip
```

> 配置 pip源地址

```shell
mkdir -p ~/.pip

cat > ~/.pip/pip.conf <<EOF
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
[install]
use-mirrors = true
mirrors = https://mirrors.aliyun.com/pypi/simple
trusted-host = mirrors.aliyun.com
EOF
```

### 安装依赖开发库

> 依赖包安装位置

```shell
# MAC
/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages
# WINDOWS
C:\Users\codepasser\AppData\Local\Programs\Python\Python38\Lib\site-packages
# CENTOS
/usr/local/lib/python3.6/site-packages
/usr/local/lib64/python3.6/site-packages

/usr/local/lib/python3/lib/python3.8/site-packages
```

#### 安装 `pyyaml`

```shell
pip3 install pyyaml
```

#### 安装 `ntplib`

```shell
pip3 install ntplib
```

#### 安装 `beautifulsoup4`

```shell
pip3 install beautifulsoup4
```

#### 安装 `pyquery`

```shell
pip3 install pyquery
```

#### 安装 `scipy` `numpy` `matplotlib`

- 正态分布依赖

```shell
pip3 install scipy
pip3 install numpy
pip3 install matplotlib #-- 图形服务器可选择安装
```

#### 安装 `flask`

```shell
pip3 install flask
pip3 install flask_restful
pip3 install fastapi
pip3 install pydantic
pip3 install uvicorn
```

#### 安装 `pymysql`

```shell
pip3 install pymysql
pip3 install cryptography
pip3 install dbutils
pip3 install sqlparse
```

#### 安装 ipython [TODO 暂未使用]

```
// 系统自带的
pip install ipython
//brew安装的
pip3 install ipython
```

### 构建打包应用 `MAC`

> 1. 下载安装 `py2app`

```shell
pip3 install py2app
```

> 2. 创建 `setup.py` 文件

```shell
py2applet --make-setup src/main.py
```

> 3. 发布应用

```shell
python3 setup.py py2app
```

### 构建打包应用 `WINDOWS`

> 1. 下载安装 pyinstaller

```shell
# 用Pyinstaller 打包程序时出现错误：
# Building PYZ because PYZ-00.toc is non existent
# ....
# TypeError: an integer is required (got type bytes).
# 出现该问题的原因是python 3.8 与 pyinstaller 3.5 不兼容。
# 直接安装最新开发版

pip3 install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
pip3 install https://github.com/pyinstaller/pyinstaller/tarball/develop
```

> 2. 发布应用

```shell
pyinstaller -F -D -c src/crawler.py
```
