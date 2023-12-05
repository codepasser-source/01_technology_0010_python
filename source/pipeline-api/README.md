# Codepasser Io Platform | Docsify

- Codepasser[Joker.Cheng]

--- 

## Python

### Python官网

#### [官网网站](https://www.python.org/)

#### [版本下载](https://www.python.org/downloads/)

> 3.8.0

- [python-3.8.0 source](https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz)
- [python-3.8.0 macOS](https://www.python.org/ftp/python/3.8.0/python-3.8.0-macosx10.9.pkg)
- [python-3.8.0 window amd64](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe)

> 3.9.0

- [python-3.9.0 source](https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz)
- [python-3.9.0 macOS](https://www.python.org/ftp/python/3.9.0/python-3.9.0-macosx10.9.pkg)
- [python-3.9.0 window amd64](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)

### Python安装

#### Windows

```shell
3.9.0
# WINDOW
https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe
```

#### Mac

```shell
# MAC
https://www.python.org/ftp/python/3.9.0/python-3.9.0-macosx10.9.pkg
# 确认安装
# MAC系统自带的python2.7，目录为
which python
/usr/bin/python
# 手动安装目录为: /usr/local/bin/python3
which python3
/Library/Frameworks/Python.framework/Versions/3.9.0/bin/python3
# 版本检查

pip3 -V
# pip 20.2.3 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)

python3 -V
# Python 3.9.0
```

> 安装 pip

```
# 安装Python2.7以上版本，会自动带pip。
# 系统自带的python没有pip，只有easy_install

# 给系统的python安装pip
easy_install pip
# 卸载 手动删除文件
easy_install -m pip
```

#### CentOS

> yum 安装

```shell
# Python2
yum install python2
# Python3
yum install python3
```

> 手动安装

- 编译安装

```shell
# 依赖
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

# cd /usr/local/lib/python
./configure --prefix=/usr/local/lib/python
make && make install
```

- 依托系统管理版本

```shell
alternatives --list
# 手动安装
alternatives --install /usr/bin/python3 python3 /usr/local/lib/python/bin/python3 60
alternatives --config python3
alternatives --install /usr/bin/pip3 pip3 /usr/local/lib/python/bin/pip3 60
alternatives --config pip3

alternatives --install /usr/bin/python python /usr/local/lib/python/bin/python3 60
alternatives --config python
alternatives --install /usr/bin/pip pip /usr/local/lib/python/bin/pip3 60
alternatives --config pip

alternatives --remove python3 /usr/local/lib/python/bin/python3
alternatives --remove pip3 /usr/local/lib/python/bin/pip3

alternatives --remove python /usr/local/lib/python/bin/python3
alternatives --remove pip /usr/local/lib/python/bin/pip3

# 配置yum 把 #! /usr/bin/python 修改为 #! /usr/bin/python2
vi /usr/bin/yum 
vi /usr/libexec/urlgrabber-ext-down 
vi /usr/bin/yum-config-manager
```

- 环境变量

```shell
export PYTHON_HOME=/usr/local/lib/python
export PYTHON_BIN=$PYTHON_HOME/bin
export PATH=$PATH:$PYTHON_BIN
```

> 配置 `pip` 源

- 常用源地址

```properties
# 阿里：https://mirrors.aliyun.com/pypi/simple
# 豆瓣：https://pypi.douban.com/simple
# 中国科技大学 ：https://pypi.mirrors.ustc.edu.cn/simple/
# 清华大学： https://pypi.tuna.tsinghua.edu.cn/simple/
# 中国科学技术大学 ：https://pypi.mirrors.ustc.edu.cn/simple/
```

- 配置

```shell
mkdir -p ~/.pip
cd ~/.pip
```

```shell
cat > ~/.pip/pip.conf <<EOF
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
[install]
use-mirrors = true
mirrors = https://mirrors.aliyun.com/pypi/simple
trusted-host = mirrors.aliyun.com
EOF
```

### 依赖包安装位置

#### `Windows`

```shell
# WINDOWS
C:\Users\codepasser\AppData\Local\Programs\Python\Python38\Lib\site-packages
```

#### `MAC`

```shell
# python 3.8
/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages

# python 3.9
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages
```

#### `CentOS`

```shell
# 系统默认版本
/usr/local/lib/python3.6/site-packages
/usr/local/lib64/python3.6/site-packages
# 手动安装版本
/usr/local/lib/python/lib/python3.8/site-packages
/usr/local/lib/python/lib/python3.9/site-packages
```

### 虚拟环境

#### 安装 `virtualenv`

```shell
pip3 install virtualenv
```

#### 创建 `Venv`

```shell
python3 -m venv venv
```

#### 激活 `Venv`

```shell
source venv/bin/activate
```

#### 退出 `Venv`

```shell
deactivate
```

- [注：`Venv` 为 `Python` 虚拟环境，创建后可独立控制`python`以及各依赖库版本，使用需要使用 `source venv/bin/active` 激活]

### 常用依赖

#### 常见错误

- [pip3 install Warning]

```shell
pip3 install --upgrade pip
```

- [ERROR: Can not execute `setup.py` since setuptools is not available in the build environment.]

```shell
pip3 install --upgrade setuptools
```

- [<twisted.python.failure.Failure
  OpenSSL.SSL.Error: [(‘SSL routines’, ‘’, ‘unsafe legacy renegotiation disabled’)]>]

```shell
# 方法一：指定版本
pip3 install cryptography==36.0.2
pip3 install pyopenssl==21.0.0
```

```shell
# 方法二：添加 openssl.conf 文件，配置启动环境变量 export OPENSSL_CONF=${PWD}/../crawler/config/openssl.conf
openssl_conf = openssl_init

[openssl_init]
ssl_conf = ssl_sect

[ssl_sect]
system_default = system_default_sect

[system_default_sect]
Options = UnsafeLegacyRenegotiation
```

#### 安装 `requests`

```shell
pip3 install requests
```

#### 安装 `PyYAML`

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
pip3 install query-string
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
pip3 install dbutils
pip3 install sqlparse
```

#### 版本记录

```shell
pip3 install requests
pip3 install pyyaml
pip3 install ntplib
pip3 install beautifulsoup4
pip3 install pyquery
pip3 install query-string
pip3 install scipy
pip3 install numpy
pip3 install matplotlib
pip3 install flask
pip3 install flask_restful
pip3 install fastapi
pip3 install pydantic
pip3 install uvicorn
pip3 install pymysql
pip3 install dbutils
pip3 install sqlparse
```

```shell
codepasser@chengyydeMacBook-Pro site-packages % pip3 list
Package               Version    
--------------------- -----------
aniso8601             9.0.1      
anyio                 3.6.2      
attrs                 22.1.0     
Automat               22.10.0    
beautifulsoup4        4.11.1     
certifi               2022.9.24  
cffi                  1.15.1     
charset-normalizer    2.1.1      
click                 8.1.3      
constantly            15.1.0     
contourpy             1.0.6      
cryptography          36.0.2     
cssselect             1.2.0      
cycler                0.11.0     
DBUtils               3.0.2      
fake-useragent        1.1.0      
Faker                 15.3.3     
fastapi               0.88.0     
filelock              3.8.0      
Flask                 2.2.2      
Flask-RESTful         0.3.9      
fonttools             4.38.0     
h11                   0.14.0     
hyperlink             21.0.0     
idna                  3.4        
importlib-metadata    5.1.0      
importlib-resources   5.10.0     
incremental           22.10.0    
itemadapter           0.7.0      
itemloaders           1.0.6      
itsdangerous          2.1.2      
Jinja2                3.1.2      
jmespath              1.0.1      
kiwisolver            1.4.4      
lxml                  4.9.1      
MarkupSafe            2.1.1      
matplotlib            3.6.2      
ntplib                0.4.0      
numpy                 1.23.5     
packaging             21.3       
parsel                1.7.0      
Pillow                9.3.0      
pip                   19.2.3     
Protego               0.2.1      
pyasn1                0.4.8      
pyasn1-modules        0.2.8      
pycparser             2.21       
pydantic              1.10.2     
PyDispatcher          2.0.6      
PyMySQL               1.0.2      
pyOpenSSL             21.0.0     
pyparsing             3.0.9      
pyquery               1.4.3      
python-dateutil       2.8.2      
pytz                  2022.6     
PyYAML                6.0        
queuelib              1.6.2      
requests              2.28.1     
requests-file         1.5.1      
scipy                 1.9.3      
Scrapy                2.7.1      
scrapy-fake-useragent 1.4.4      
scrapyd               1.3.0      
scrapyd-client        1.2.2      
service-identity      21.1.0     
setuptools            41.2.0     
six                   1.16.0     
sniffio               1.3.0      
soupsieve             2.3.2.post1
sqlparse              0.4.3      
starlette             0.22.0     
tldextract            3.4.0      
Twisted               22.10.0    
typing-extensions     4.4.0      
uberegg               0.1.1      
urllib3               1.26.13    
uvicorn               0.20.0     
w3lib                 2.1.0      
Werkzeug              2.2.2      
zipp                  3.11.0     
zope.interface        5.5.2
```

### 卸载

#### `MAC` 环境卸载

> `Applications` 中删除

> 手动删除文件

```shell
sudo rm -rf /usr/local/bin/pip3
sudo rm -rf /usr/local/bin/pip3.8
sudo rm -rf /usr/local/bin/python3
sudo rm -rf /usr/local/bin/python3-config
sudo rm -rf /usr/local/bin/python3.8
sudo rm -rf /usr/local/bin/python3.8-config
sudo rm -rf /usr/local/bin/pydoc3
sudo rm -rf /usr/local/bin/pydoc3.8
sudo rm -rf /usr/local/bin/easy_install-3.8
sudo rm -rf /usr/local/bin/2to3
sudo rm -rf /usr/local/bin/2to3-3.8
sudo rm -rf /usr/local/bin/idle3
sudo rm -rf /usr/local/bin/idle3.8
sudo rm -rf /Library/Frameworks/Python.framework
```