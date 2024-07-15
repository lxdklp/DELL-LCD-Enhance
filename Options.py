import psutil
import time
import requests
from mcstatus import JavaServer
import paho.mqtt.client as mqtt
from datetime import datetime
from log import *
from Execute import *

# CPU
def cpu ():
    cpu = psutil.cpu_percent(interval=1)
    cmd = "racadm set System.LCD.UserDefinedString " + '"CPU used:' + str(cpu) + '%"'
    info = execute(cmd)
    if info == "Object value modified successfully":
        log(0,"成功推送CPU占用,数据为" + cpu)
    elif info == "ERROR: Unable to perform requested operation.":
        log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
    else:
        log(2,"未知错误:" + str(info))

# 内存
def mem ():
    mem = psutil.virtual_memory()
    mem = mem.percent 
    cmd = "racadm set System.LCD.UserDefinedString " + '"MEM used:' + str(mem) + '%"'
    info = execute(cmd)
    info.rstrip()
    if info == "Object value modified successfully":
        log(0,"成功推送内存占用,数据为" + mem)
    elif info == "ERROR: Unable to perform requested operation.":
        log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
    else:
        log(2,"未知错误:" + str(info))

# 启动时间
def bootTime():
    time = psutil.boot_time()
    str(time)
    cmd = "racadm set System.LCD.UserDefinedString " + '"Boot Time:' + str(time) + '"'
    info = execute(cmd)
    info.rstrip()
    if info == "Object value modified successfully":
        log(0,"成功推送启动时间,数据为" + time)
    elif info == "ERROR: Unable to perform requested operation.":
        log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
    else:
        log(2,"未知错误:" + str(info))

# 硬盘
def disk(path):
    disk = psutil.disk_usage(path)
    disk = disk.percent
    cmd = "racadm set System.LCD.UserDefinedString " + path + '" used:' + str(disk) + '%"'
    info = execute(cmd)
    info.rstrip()
    if info == "Object value modified successfully":
        log(0,"成功推送" + path + "盘占用,数据为" + disk)
    elif info == "ERROR: Unable to perform requested operation.":
        log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
    else:
        log(2,"未知错误:" + str(info))

# Minecraft服务器在线人数
def mcOnline(ip):
    try:
        server = JavaServer.lookup(ip)
        server = server.status()
        server = server.players.online
        server = str(server)
        cmd = "racadm set System.LCD.UserDefinedString " + '"Online:' + str(server) + '"'
        info = execute(cmd)
        info.rstrip()
        if info == "Object value modified successfully":
            log(0,"成功推送Minecraft服务器在线人数,数据为" + server)
        elif info == "ERROR: Unable to perform requested operation.":
            log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
        else:
            log(2,"未知错误:" + str(info))
    except Exception as e:
        log(2, f"推送Minecraft服务器在线人数时发生错误: {e}")

# Minecraft服务器延时
def mcPing(ip):
    try:
        server = JavaServer.lookup(ip)
        server = server.status()
        server = server.players.ping
        server = str(server)
        cmd = "racadm set System.LCD.UserDefinedString " + '"Ping:' + str(server) + 'ms"'
        info = execute(cmd)
        info.rstrip()
        if info == "Object value modified successfully":
            log(0,"成功推送Minecraft服务器延时,数据为" + server)
        elif info == "ERROR: Unable to perform requested operation.":
            log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
        else:
            log(2,"未知错误:" + str(info))
    except Exception as e:
        log(2, f"推送Minecraft服务器延时时发生错误: {e}")

# MQTT
# 当接收到消息时的回调函数
def on_message(client, userdata, message):
    global msg
    msg = message.payload.decode("utf-8")
def quickMqtt(ip, port, topic, delay):
    global msg
    msg = None
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(ip, port, 60)
    client.subscribe(topic)
    client.loop_start()
    time.sleep(delay)
    client.loop_stop()
    client.disconnect()
    # 如果接收到了消息
    if msg is not None:
        msg = str(msg).strip('{}')
        return 1,msg
    # 如果没有接收到消息
    else:
        return 1, msg

# HTTP请求
def httpGet(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            log(1, f"请求失败,状态码: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        log(2, f"发生错误: {e}")
        return None
    
# 自定义信息
def userMsg(msg):
    str(msg)
    cmd = "racadm set System.LCD.UserDefinedString " + msg + '"'
    info = execute(cmd)
    info.rstrip()
    if info == "Object value modified successfully":
        log(0,"成功推送自定义信息,信息为" + msg)
    elif info == "ERROR: Unable to perform requested operation.":
        log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
    else:
        log(2,"未知错误:" + str(info))