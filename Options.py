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
    cpu = str(cpu)
    cmd = "racadm set System.LCD.UserDefinedString " + '"CPU used:' + cpu + '%"'
    info = execute(cmd)
    if info == "Object value modified successfully":
        log(0,"成功推送CPU占用,数据为" + cpu)
    elif info == "ERROR: Unable to perform requested operation.":
        log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
    else:
        log(2,"推送信息至LCD面板时发生未知错误:" + str(info))

# 内存
def mem ():
    mem = psutil.virtual_memory()
    mem = mem.percent 
    mem = str(mem)
    cmd = "racadm set System.LCD.UserDefinedString " + '"MEM used:' + mem + '%"'
    info = execute(cmd)
    info.rstrip()
    if info == "Object value modified successfully":
        log(0,"成功推送内存占用,数据为" + mem)
    elif info == "ERROR: Unable to perform requested operation.":
        log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
    else:
        log(2,"推送信息至LCD面板时发生未知错误:" + str(info))

# 启动时间
def bootTime():
    time = psutil.boot_time()
    time = str(time)
    cmd = "racadm set System.LCD.UserDefinedString " + '"Boot Time:' + time + '"'
    info = execute(cmd)
    info.rstrip()
    if info == "Object value modified successfully":
        log(0,"成功推送启动时间,数据为" + time)
    elif info == "ERROR: Unable to perform requested operation.":
        log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
    else:
        log(2,"推送信息至LCD面板时发生未知错误:" + str(info))

# 硬盘
def disk(path):
    disk = psutil.disk_usage(path)
    disk = disk.percent
    disk = str(disk)
    cmd = "racadm set System.LCD.UserDefinedString " + path + '" used:' + disk + '%"'
    info = execute(cmd)
    info.rstrip()
    if info == "Object value modified successfully":
        log(0,"成功推送" + str(path) + "盘占用,数据为" + disk)
    elif info == "ERROR: Unable to perform requested operation.":
        log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
    else:
        log(2,"推送信息至LCD面板时发生未知错误:" + str(info))

# Minecraft服务器在线人数
def mcOnline(ip,port,minecraftOn):
    if minecraftOn == True:
        try:
            online = JavaServer.lookup(ip + ":" + port)
            online = online.status()
            online = online.players.online
            online = str(online)
            cmd = "racadm set System.LCD.UserDefinedString " + '"Online:' + str(online) + '"'
            info = execute(cmd)
            info.rstrip()
            if info == "Object value modified successfully":
                log(0,"成功推送Minecraft服务器在线人数,数据为" + online)
            elif info == "ERROR: Unable to perform requested operation.":
                log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
            else:
                log(2,"推送信息至LCD面板时发生未知错误:" + str(info))
        except Exception as e:
            log(2, f"推送Minecraft服务器在线人数时发生错误: {e}")
    if minecraftOn == False:
        log(2,"未在配置文件中启用Minecraft服务器")

# Minecraft服务器延时
def mcPing(ip, port, minecraftOn):
    if minecraftOn == 1:
        try:
            ping = JavaServer.lookup(ip + ":" + str(port))
            ping = ping.ping()
            ping = str(int(ping))
            cmd = "racadm set System.LCD.UserDefinedString " + '"Ping:' + ping + 'ms"'
            info = execute(cmd)
            info.rstrip()
            if info == "Object value modified successfully":
                log(0,"成功推送Minecraft服务器延时,数据为" + ping)
            elif info == "ERROR: Unable to perform requested operation.":
                log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
            else:
                log(2,"推送信息至LCD面板时发生未知错误:" + str(info))
        except Exception as e:
            log(2, f"推送Minecraft服务器延时时发生错误: {e}")
    if minecraftOn == False:
        log(2,"未在配置文件中启用Minecraft服务器")

# MQTT
# 当接收到消息时的回调函数
def on_message(client, userdata, message):
    global msg
    msg = message.payload.decode("utf-8")
def quickMqtt(ip, port, topic, delay, mqttOn):
    if mqttOn == True:
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
            cmd = "racadm set System.LCD.UserDefinedString " + '"' + msg + '"'
            info = execute(cmd)
            if info == "Object value modified successfully":
                log(0,"已接收到新的MQTT讯息,并且成功推送到LCD面板,数据为" + msg)
                msg = None
                time.sleep(delay)
            elif info == "ERROR: Unable to perform requested operation.":
                log(2,"已接收到新的MQTT讯息,但是没有推送到LCD面板,请检测服务器LCD面板是否设置为自定义字符串模式")
                msg = None
            else:
                log(2,"已接收到新的MQTT讯息,但是推送信息至LCD面板时发生未知错误:" + str(info))
                msg = None
        # 如果没有接收到消息
        else:
            log(0,"未收到新的MQTT讯息")
    if mqttOn == False:
        time.sleep(delay)

# HTTP请求
def httpGet(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            msg = str(response.text)
            cmd = "racadm set System.LCD.UserDefinedString " + '"' + msg + '"'
            info = execute(cmd)
            info.rstrip()
            if info == "Object value modified successfully":
                log(0,"成功请求" + url + ",数据为" + msg)
            elif info == "ERROR: Unable to perform requested operation.":
                log(2,"请检测服务器LCD面板是否设置为自定义字符串模式")
            else:
                log(2,"推送信息至LCD面板时发生未知错误:" + str(info))
        else:
            log(1, "请求" + url + f"时失败,状态码: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        log(2,"请求" + url +  f"时发生错误: {e}")
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
        log(2,"推送信息至LCD面板时发生未知错误:" + str(info))