<script setup lang="ts">
import axios from 'axios'
import dayjs from 'dayjs'
import { ClearOutlined, LoadingOutlined } from '@ant-design/icons-vue'
import { useStorage } from '@vueuse/core'
import Message from './components/message.vue'

const loadding = ref(false)

const message = ref('')
const messages = useStorage('messages', [
  {
    username: "chatGPT",
    msg: "Hello, I'm chatGPT",
    time: dayjs().format('HH:mm'),
    type: 0,
  },
])

const apiCompletion = async (text: string) => {
  const res = await axios.post('/completions', {
    model: 'text-davinci-003',
    prompt: text,
    max_tokens: 2048,
    temperature: 0.5,
    frequency_penalty: 0,
    presence_penalty: 0,
    top_p: 1,
  })
  return res
}

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
  const res = await apiCompletion(text)
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
