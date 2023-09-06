FROM python:3.8-bullseye
# settings timezone
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

# settings container
WORKDIR /usr/src/app
VOLUME /usr/src/logs
EXPOSE 8021

# settings python environment
RUN mkdir -p ~/.pip
RUN cd ~/.pip
RUN cat > ~/.pip/pip.conf <<EOF
[global]
index-url = https://mirrors.aliyun.com/pypi/simple
[install]
use-mirrors = true
mirrors = https://mirrors.aliyun.com/pypi/simple
trusted-host = mirrors.aliyun.com
EOF

# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install requests
RUN pip install pyyaml
RUN pip install ntplib
RUN pip install beautifulsoup4
RUN pip install pyquery
RUN pip install query-string
RUN pip install scipy
RUN pip install numpy
RUN pip install matplotlib
RUN pip install flask
RUN pip install flask_restful
RUN pip install fastapi
RUN pip install pydantic
RUN pip install uvicorn
RUN pip install pymysql
RUN pip install dbutils
RUN pip install sqlparse
RUN pip list

# run application
CMD ./run.sh start

