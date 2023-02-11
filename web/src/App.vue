<script setup lang="ts">
import dayjs from 'dayjs'
import { ClearOutlined, LoadingOutlined, RedoOutlined } from '@ant-design/icons-vue'
import { useStorage } from '@vueuse/core'
import { completion, creditSummary } from '@/api'
import Message from './components/message.vue'

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
  const res = await completion(text)
  messages.value.push({
    username: "chatGPT",
    msg: res.data.choices[0].text,
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
        <div class="px-10 py-5">
          <Message :message=message v-for="message in messages" :class="message.type ? 'send' : 'replay'" />
        </div>
      </main>
      <footer id="footer">
        <div class="px-4 rounded-lg bg-light-100">
          <a-textarea v-model:value="message" :rows="4" @pressEnter="sendMessage" placeholder="请输入消息..."></a-textarea>
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
