## 代理相关问题：

国内由于网络原因，访问API时候需要使用代理。这里图示说明下如何使用代理。

下面我将以`clash`为例。首先你得确保在本机使用代理情况可以访问api。

![](https://miclon-job.oss-cn-hangzhou.aliyuncs.com/img/20230307222327.png)


如果你的`MacOS`或者`windows`系统，你需要将docker容器中的代理地址设置为局域网地址。

具体查看局域网IP地址：

mac上执行 `ifconfig`，win上执行 `ipconfig`

```bash
docker run --name chatgpt -d -p 8000:8000 -e API_KEY=sk-xxxx -e HTTPS_PROXY=http://你的局域网IP:代理端口 miclon/chatgpt:latest
```

示例：
```bash
docker run --name chatgpt -d -p 8000:8000 -e API_KEY=sk-xxxx -e HTTPS_PROXY=http://192.168.0.10:7890 miclon/chatgpt:latest
```

如果你是Linux系统，你可以直接使用：

```bash
docker run --name chatgpt -d -p 8000:8000 -e API_KEY=sk-xxxx -e HTTPS_PROXY=http://127.0.0.1:7890 miclon/chatgpt:latest
```

* 注意：上文中端口都是`7890`，具体按你实际情况填写。
* 注意关闭本机防火墙。
