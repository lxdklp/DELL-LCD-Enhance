from datetime import datetime
import os
import glob

def log (limit,lv,msg):
    # 日志记录等级限制
    if lv <= limit:
        return

    # 日志等级
    if lv == 1:
        lv = "[INFO]"
    if lv == 2:
        lv = "[WARN]"
    if lv == 3:
        lv = "[ERROR]"
    
    # 整理日志格式
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    msg = lv + "[" + time + "]" + msg + "\n"

    # 写入文件
    with open("./log/" + date + ".log", "a",encoding="utf-8") as f:
        f.write(msg)

def delLog(limit, saveTime):
    # 获取当前日期
    currentDate = datetime.now()

    # 查找所有 log 文件
    logFiles = glob.glob(os.path.join("./log/", "*.log"))

    for logFile in logFiles:
        # 获取文件创建时间
        creationTime = os.path.getctime(logFile)
        creationDate = datetime.fromtimestamp(creationTime)

        # 计算文件创建日期与当前日期的差距
        days_difference = (currentDate - creationDate).days

        # 如果超过 saveTime 天，则删除文件
        if days_difference > saveTime:
            os.remove(logFile)
            log(limit, 1, f"删除旧日志文件: {logFile}")