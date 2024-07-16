# 这里是"disk"项的解释
* **"disk"** 也是一个数列,它记录了要显示的硬盘与顺序
## 例子
我要先显示C盘然后显示D盘
首先确保 `"lcd"` 中有两个 `"disk"`  
```json
"lcd":[
        "disk",
        "disk"
]
```
然后在 `"disk"` 中按顺序添加路径
```json
"disk":[
        "C:",
        "D:"
]
```