# 这里是"setting"项的解释
"setting"下有 [**"delay"**](https://github.com/lxdklp/DELL-LCD-Enhance/wiki/setting%E9%A1%B9#delay) [**"mqtt"**](https://github.com/lxdklp/DELL-LCD-Enhance/wiki/setting%E9%A1%B9#mqtt) [**"minecraft"**](https://github.com/lxdklp/DELL-LCD-Enhance/wiki/setting%E9%A1%B9#minecraft) 3个对象
## "delay"
数据类型为整数,决定了你LCD面板更新每个项目的延时  
*注意,真正的显示时间应该是delay加上racadm命令的执行时间*
## "mqtt"
"mqtt"决定了MQTT客户端相关配置,下面有4个对象
1. "mqtt on"
    - 布尔类型
    - 这个决定了是否启用MQTT客户端
    - 如果设置为False可以不填写下面两项
2. "IP"
    - 字符串
    - 这里填入你MQTT服务器的IP\域名
3. "PORT"
    - 整数
    - 这里填入你MQTT服务器的端口
4. "TOPIC"
    - 字符串
    - 这里填入你要监听的MQTT主题
##  "minecraft"
"minecraft"决定了Minecraft客户端相关配置,下面有3个对象
1. "minecraft on"
    - 布尔类型
    - 这个决定了是否启用Minecraft服务器监视
    - 如果设置为False可以不填写下面两项
2. "IP"
    - 字符串
    - 这里填入你Minecraft服务器的IP\域名
3. "PORT"
    - 整数
    - 这里填入你Minecraft服务器的端口