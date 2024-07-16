# 这里是"userMsg"项的解释
* **"userMsg"** 也是一个数列,它记录了要显示的自定义文本与顺序
## 例子
我要先显示`lxdklp`然后再显示`114514`  
首先确保 `"lcd"` 中有两个 `"userMsg"`  
```json
"lcd":[
        "userMsg",
        "userMsg"
]
```
然后在 `"userMsg"` 中按顺序添加链接
```json
"userMsg":[
        "lxdklp",
        "114514"
]
```