import json
from Options import *
from log import *

log(0,1,"启动程序")

# 读取配置文件
with open("config.json", "r") as f:
    config = json.load(f)

# 读取日志设置
limit = config["setting"]["log"]["lv"]
autoDel = config["setting"]["log"]["autoDel"]
if autoDel == True:
    log(limit,1,"已启用日志自动删除")
    saveTime = config["setting"]["log"]["save time"]
if autoDel == False:
    log(limit,1,"未启用日志自动删除")
    saveTime = None

# 读取延时设置
delay = config["setting"]["delay"]

# 读取MQTT
mqttOn = config["setting"]["mqtt"]["mqtt on"]
if mqttOn == True:
    mqttIP = config["setting"]["mqtt"]["IP"]
    mqttPORT = config["setting"]["mqtt"]["PORT"]
    mqttTOPIC = config["setting"]["mqtt"]["TOPIC"]
    mqttIP = str(mqttIP)
    log(limit,1,"已读取MQTT配置,IP:" + mqttIP + ",端口:" + str(mqttPORT) + ",监听主题:" + mqttTOPIC)
if mqttOn == False:
    mqttIP = None
    mqttPORT = None
    mqttTOPIC = None
    log(limit,1,"MQTT服务器未启用")

# 读取Minecraft
minecraftOn = config["setting"]["minecraft"]["minecraft on"]
if minecraftOn == True:
    minecraftIP = config["setting"]["minecraft"]["IP"]
    minecraftPORT = config["setting"]["minecraft"]["PORT"]
    minecraftPORT = str(minecraftPORT)
    log(limit,1,"已读取Minecraft配置,IP:" + str(minecraftIP) + ",端口" + str(minecraftPORT))
if minecraftOn == False:
    minecraftIP = None
    minecraftPORT = None
    log(limit,1,"Minecraft服务器未启用")

# 读取显示项
lcdQueue = len(config["lcd"])
lcdDisplay = 0
log(limit,1,"已读取到共有" + str(lcdQueue) + "个显示项")

# 读取磁盘配置
diskQueue = len(config["disk"])
diskDisplay = 0
log(limit,1,"已读取到共有" + str(diskQueue) + "个磁盘")

# 读取HTTP请求配置
urlQueue = len(config["url"])
urlDisplay = 0
log(limit,1,"已读取到共有" + str(urlQueue) + "个HTTP请求")

# 读取用户自定义信息配置
userMsgQueue = len(config["userMsg"])
userMsgDisplay = 0
log(limit,1,"已读取到共有" + str(userMsgQueue) + "个用户自定义信息")

# 主循环
while 1:
    item = config["lcd"][lcdDisplay]
    # 执行
    if item == "cpu":
        cpu(limit)
    if item == "mem":
        mem(limit)
    if item == "bootTime":
        bootTime(limit)
    if item == "disk":
        path = config["disk"][diskDisplay]
        if diskDisplay == diskQueue -1:
            diskDisplay = 0
        else:
            diskDisplay = diskDisplay + 1
        disk(limit,path)
    if item == "mcOnline":
        mcOnline(limit,minecraftIP, minecraftPORT ,minecraftOn)
    if item == "mcPing":
        mcPing(limit,minecraftIP, minecraftPORT ,minecraftOn)
    if item == "httpGet":
        url = config["url"][urlDisplay]
        httpGet(limit,url)
        if urlDisplay == urlQueue -1:
            urlDisplay = 0
        else:
            urlDisplay = urlDisplay + 1
    if item == "userMsg":
        msg = config["userMsg"][userMsgDisplay]
        userMsg(limit,msg)
        if userMsgDisplay == userMsgQueue -1:
            userMsgDisplay = 0
        else:
            userMsgDisplay = userMsgDisplay + 1
    # 等待或接收MQTT讯息
    quickMqtt(limit,mqttIP, mqttPORT, mqttTOPIC, delay, mqttOn)
    # 循环计数
    if lcdDisplay == lcdQueue - 1:
        lcdDisplay = 0
    else:
        lcdDisplay = lcdDisplay + 1
    # 日志自动删除
    delLog(limit,saveTime)