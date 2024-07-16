# 这里是"url"项的解释
* **"url"** 也是一个数列,它记录了要请求的链接与顺序
## 例子
我要先请求`https://lxdklp.top`然后再请求`https://api.lxdklp.top`  
首先确保 `"lcd"` 中有两个 `"httpGet"`  
```json
"lcd":[
        "httpGet",
        "httpGet"
]
```
然后在 `"url"` 中按顺序添加链接
```json
"url":[
        "https://lxdklp.top",
        "https://api.lxdklp.top"
]
```