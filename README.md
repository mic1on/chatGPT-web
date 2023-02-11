## ChatGPT-WEB

![](https://miclon-job.oss-cn-hangzhou.aliyuncs.com/img/20230210145121.png)
本项目为`chatgpt`私有化部署，基于`fastapi` `vue3` `chatgpt api`实现。



- [笔者案例 - 我用AI帮我完成了单子](https://52caiji.com/posts/other/developer-use-openai.html)

## 快速开始

### 1. docker 部署
作者已经将`chatgpt`打包成镜像，可以直接使用`docker`部署。

```bash
docker run --name chatgpt -d -p 8000:8000 -e API_KEY=xxxxxx miclon/chatgpt:latest
```

### 2. 本地部署

- 拉取项目，安装依赖

```bash
cd web
pnpm install
```

```bash
cd api
pip install -r requirements.txt
```

- 启动项目


```bash
# 启动前端
cd web
pnpm run dev
```

```bash
# 启动后端
cd api
python app.py
```

## 如果你不想动手

笔者自建了微信公众号：**代码领悟**，您关注后即可直接与AI对话。

公众号搭建chatGPT搭建流程图：

![](https://miclon-job.oss-cn-hangzhou.aliyuncs.com/img/20230210220109.png)


## 答疑

- 为什么需要`API_KEY`？

`API_KEY`是`chatgpt`的API密钥，通过API_KEY方可调用官方接口，您可以在[chatgpt](https://platform.openai.com/account/api-keys)官网申请。`API_KEY`通常是`sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`这种形式。

- 我想修改项目中版权信息，如何修改？

如果你不懂前端，你可以直接fork项目，替换前端字符串然后提交自己仓库，然后会自动docker构建。但是有个前提，你需要在github actions中配置`DOCKER_USERNAME`和`DOCKER_PASSWORD`，这两个变量是你的docker账号和密码。

- 为什么要内置后端？

前端其实可以直接通过`axios`请求`chatgpt`官方接口，但是为了数据安全，如果前端调用那就会暴露自己的`API_KEY`，所以笔者将前端和后端分离，前端只负责展示，后端负责调用`chatgpt`官方接口。
