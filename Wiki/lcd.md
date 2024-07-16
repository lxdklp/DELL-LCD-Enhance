# 这里是"lcd"项的解释
* `"lcd"` 是一个数列，它记录着LCD面板显示的顺序
* `"lcd"` 下的项目可以重复, `"disk"` `"httpGet"` `"userMsg"` 这些特殊项多次遇到时显示不同数据,详细请进入对应页面查看
* `lcd` 下的项目均为字符串
* 目前 `"lcd"` 支持以下项目
    -  `"cpu"` 显示CPU的占用率
    -  `"mem"` 显示内存占用率
    -  `"bootTime"` 显示启动时间
    -  `"disk"` 显示硬盘占用率,详细请前往 [`"disk项"`](https://github.com/lxdklp/DELL-LCD-Enhance/wiki/disk%E9%A1%B9) 查看
    -  `"mcOnline"` 显示Minecraft服务器在线人数
    -  `"mcPing"` 显示Minecraft服务器延时
    -  `"httpGet"` 显示HTTP请求到的数据,详细请前往 [`"url项"`](https://github.com/lxdklp/DELL-LCD-Enhance/wiki/url%E9%A1%B9) 查看
    -  `"userMsg"` 显示自定义字符串,详细请前往 [`"userMsg项"`](https://github.com/lxdklp/DELL-LCD-Enhance/wiki/userMsg%E9%A1%B9) 查看

`*
## 例子
我想要按CPU-内存-硬盘的顺序显示
```json
"lcd":[
        "cpu",
        "mem",
        "disk"
]
```