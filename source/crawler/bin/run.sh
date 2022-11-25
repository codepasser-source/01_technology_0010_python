#!/bin/bash
SERV_NAME=application
# PID  代表是PID文件
PID=$SERV_NAME.pid
# PROFILE
export CRAWLER_PROFILE=uat

# 使用说明，用来提示输入参数
usage() {
  echo "Usage: sh 执行脚本.sh [start|stop|restart|status]"
  exit 1
}

# 检查程序是否在运行
is_exist() {
  pid=$(ps -ef | grep ${SERV_NAME} | grep -v grep | awk '{print $2}')
  # 如果不存在返回1，存在返回0
  if [ -z "${pid}" ]; then
    return 1
  else
    return 0
  fi
}

# 启动
start() {
  echo "Start: sh 执行脚本.sh [start]"
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> ${SERV_NAME} is already running PID=${pid} <<<"
  else
    echo ">>> ${SERV_NAME} is starting PROFILE=${CRAWLER_PROFILE} <<<"
    nohup python3 $PWD/../src/application.py >/dev/null 2>&1 &
    echo $! >$PID
    echo ">>> start ${SERV_NAME} success PID=$! <<<"
    sleep 1
    # tail -fn 100 ./logs/$SERVICE_NAME/info.log
  fi
}

# 停止
stop() {
  echo "Stop: sh 执行脚本.sh [stop]"
  #is_exist
  pidf=$(cat $PID)
  #echo "$pidf"
  echo ">>> ${SERV_NAME} PID = $pidf begin kill $pidf <<<"
  kill $pidf
  rm -rf $PID
  sleep 2
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> ${SERV_NAME} 2 PID = $pid begin kill -9 $pid  <<<"
    kill -9 $pid
    sleep 2
    echo ">>> ${SERV_NAME} process stopped <<<"
  else
    echo ">>> ${SERV_NAME} is not running <<<"
  fi
}

# 状态
status() {
  echo "Status: sh 执行脚本.sh [status]"
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> ${SERV_NAME} is running PID is ${pid} <<<"
  else
    echo ">>> ${SERV_NAME} is not running <<<"
  fi
}

# 重启
restart() {
  echo "Restart: sh 执行脚本.sh [restart]"
  stop
  start
}

# 根据输入参数，选择执行对应方法，不输入则执行使用说明
case "$1" in
"start")
  start
  ;;
"stop")
  stop
  ;;
"status")
  status
  ;;
"restart")
  restart
  ;;
*)
  usage
  ;;
esac
exit 0