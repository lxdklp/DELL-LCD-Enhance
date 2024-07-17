from datetime import datetime

def log (lv,msg):
    # 日志等级
    if lv == 0:
        lv = "[INFO]"
    if lv == 1:
        lv = "[WARN]"
    if lv == 2:
        lv = "[ERROR]"

    # 整理日志格式
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    msg = lv + "[" + time + "]" + msg + "\n"

    # 写入文件
    with open("./log/" + date + ".log", "a",encoding="utf-8") as f:
        f.write(msg)