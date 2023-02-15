<script setup lang="ts">
import dayjs from 'dayjs'
import { ClearOutlined, LoadingOutlined, RedoOutlined } from '@ant-design/icons-vue'
import { useStorage } from '@vueuse/core'
import { completion, creditSummary } from '@/api'
import Message from './components/message.vue'

const createdAt = dayjs().format('YYYY-MM-DD HH:mm:ss')
const loadding = ref(false)
const summary = ref({} as any)

const message = ref('')
const messages = useStorage('messages', [
  {
    username: "chatGPT",
    msg: "Hello, I'm chatGPT",
    time: dayjs().format('HH:mm'),
    type: 0,
  },
])

const sendMessage = async () => {
  loadding.value = true
  const text = message.value
  message.value = ""
  messages.value.push({
    username: "user",
    msg: text,
    time: dayjs().format('HH:mm'),
    type: 1,
  })
  const data: any = await completion(text)
  const replyMessage = data?.choices ? data.choices[0].text : "我不知道你在说什么"
  messages.value.push({
    username: "chatGPT",
    msg: replyMessage,
    time: dayjs().format('HH:mm'),
    type: 0,
  })
  loadding.value = false
}

const clearMessages = () => {
  messages.value = []
}

const refushCredit = async () => {
  loadding.value = true
  summary.value = await creditSummary()
  loadding.value = false
}

onMounted(async () => {
  await refushCredit()
})
</script>

<template>
  <div id="layout">
    <header id="header" class="bg-dark-50 text-white h-10 select-none">
      <LoadingOutlined v-if="loadding" class="pl-3 cursor-pointer" />
      <span class="text-size-5 pl-5">chatGPT</span>
      <span class="pl-3">代码领悟</span>
      <a-tooltip>
        <template #title>清除聊天记录</template>
        <a-popconfirm title="确定清除本地所有聊天记录吗?" ok-text="是的" cancel-text="再想想" @confirm="clearMessages">
          <ClearOutlined class="pl-3 cursor-pointer" />
        </a-popconfirm>

      </a-tooltip>
      <span class="float-right pr-3 pt-2">
        当前余额：{{ summary?.total_available }}
        <a-tooltip>
          <template #title>刷新余额</template>
          <RedoOutlined @click="refushCredit" />
        </a-tooltip>
      </span>
    </header>
    <div id="layout-body">
      <main id="main">
        <div class="flex-1 relative flex flex-col">
          <!-- header -->
          <!-- content -->
          <div class="flex-1 inset-0 overflow-hidden bg-transparent bg-bottom bg-cover flex flex-col">
            <!-- dialog -->
            <div class="flex-1 w-full self-center">
              <div class="relative px-3 py-1 m-auto flex flex-col">
                <div class="mx-0 my-1 self-center text-xs text-gray-400">
                  频道已创建
                </div>
                <div class="mx-0 my-1 self-center text-xs text-gray-400">
                  {{ createdAt }}
                </div>
                <Message :message=message v-for="message in messages" :class="message.type ? 'send' : 'replay'" />
              </div>
            </div>
          </div>
        </div>
      </main>
      <footer id="footer">
        <div class="relative p-4 w-full overflow-hidden text-gray-600 focus-within:text-gray-400 flex items-center">
          <a-textarea v-model:value="message" :auto-size="{ minRows: 2, maxRows: 5 }" placeholder="请输入消息..."
            class="appearance-none pl-10 py-2 w-full bg-white border border-gray-300 rounded-full text-sm placeholder-gray-800 focus:outline-none focus:border-blue-500 focus:border-blue-500 focus:shadow-outline-blue" />
          <span class="absolute inset-y-0 right-0 bottom-8 pr-6 flex items-end">
            <a-button shape="round" type="primary" @click="sendMessage">发送</a-button>
          </span>
        </div>

      </footer>
    </div>
  </div>
</template>

<style scoped>
body,
html {
  margin: 0;
  padding: 0;
}

#layout {
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100vh;
  background-color: #f0f2f5;
}

#header {
  box-shadow: 2px 5px 5px 0px rgba(102, 102, 102, 0.5);
  flex-shrink: 0;
}

#layout-body {
  flex-grow: 2;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

#footer {
  height: 100px;
  flex-shrink: 0;
}

#main {
  flex-grow: 2;
}

.replay {
  float: left;
  clear: both;
}

.send {
  float: right;
  clear: both;
}
</style>
