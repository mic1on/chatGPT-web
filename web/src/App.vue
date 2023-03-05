<script setup lang="ts">
import dayjs from 'dayjs'
import { ClearOutlined, LoadingOutlined, RedoOutlined, SettingOutlined, GithubOutlined } from '@ant-design/icons-vue'
import { completion, creditSummary, completionTurbo } from '@/api'
import Message from './components/message.vue'
import SettingModal from './components/setting.vue'
import useSetting from '@/composables/setting'
import useMessages from '@/composables/messages'
import { TSummary } from '@/types'

const setting = useSetting()

const state = reactive({
  message: '',
  loadding: false,
  visible: false,
  summary: {} as TSummary,
})
const createdAt = dayjs().format('YYYY-MM-DD HH:mm:ss')

const messages = useMessages()


const buildMessage = () => {
  let _messages = []
  const lastMessages = messages.getLastMessages(10)

  for (let i = 0; i < lastMessages.length; i++) {
    const element = lastMessages[i]
    if (element.type === 0) {
      _messages.push("AI:\n" + element.msg)
    } else {
      _messages.push("User:\n" + element.msg)
    }
  }
  return _messages.join("\n\n") + "\n\AI:\n"
}

const sendMessage = async (event: { preventDefault: () => void }) => {
  event.preventDefault() // 阻止默认事件
  state.loadding = true
  messages.addMessage({
    username: "user",
    msg: state.message,
    type: 1,
  })
  let question = ""
  if (setting.value.continuously) {
    question = buildMessage()
  } else {
    question = "User:\n" + state.message + "\n\nAI:\n"
  }
  state.message = ""
  const data: any = setting.value.model === 'gpt-3.5-turbo' ? await completionTurbo(question) : await completion(question)
  const replyMessage = data?.choices ? (data.choices[0]?.text ? data.choices[0].text : data.choices[0].message.content) : data?.error?.message
  messages.addMessage({
    username: "chatGPT",
    msg: replyMessage,
    type: 0,
  })
  state.loadding = false
}

const clearMessages = () => {
  messages.clearMessages()
}

const totalAvailable = computed(() => {
  const total = state.summary?.total_available || 0
  return total.toFixed(2)
})
const refushCredit = async () => {
  state.loadding = true
  state.summary = await creditSummary()
  state.loadding = false
}
const handleToGithub = () => {
  window.open('https://github.com/mic1on/chatGPT-web')
}

onMounted(async () => {
  await refushCredit()
})
</script>

<template>
  <div id="layout">
    <header id="header" class="bg-dark-50 text-white h-10 select-none">
      <LoadingOutlined v-if="state.loadding" class="pl-3 cursor-pointer" />
      <span class="text-size-5 pl-5">ChatGPT</span>
      <a-tooltip>
        <template #title>清除聊天记录</template>
        <a-popconfirm title="确定清除本地所有聊天记录吗?" ok-text="是的" cancel-text="再想想" @confirm="clearMessages">
          <ClearOutlined class="pl-3 cursor-pointer" />
        </a-popconfirm>
      </a-tooltip>

      <a-tooltip>
        <template #title>设置</template>
        <SettingOutlined class="pl-3 cursor-pointer" @click="state.visible = true" />
      </a-tooltip>

      <a-tooltip>
        <template #title>开源地址</template>
        <GithubOutlined class="pl-3 cursor-pointer" @click="handleToGithub" />
      </a-tooltip>

      <span class="float-right pr-3 pt-2">
        当前余额：{{ totalAvailable }}
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
                <Message :message=msg v-for="msg in messages.messages.value"
                  :class="msg.type === 1 ? 'send' : 'replay'" />
              </div>
            </div>
          </div>
        </div>
      </main>

    </div>
    <footer id="footer">
      <div class="relative p-4 w-full overflow-hidden text-gray-600 focus-within:text-gray-400 flex items-center">
        <a-textarea v-model:value="state.message" :auto-size="{ minRows: 2, maxRows: 5 }" placeholder="请输入消息..."
          @pressEnter="sendMessage($event)"
          class="appearance-none pl-10 py-2 w-full bg-white border border-gray-300 rounded-full text-sm placeholder-gray-800 focus:outline-none focus:border-blue-500 focus:border-blue-500 focus:shadow-outline-blue" />
        <span class="absolute inset-y-0 right-0 bottom-8 pr-6 flex items-end">
          <a-button shape="round" type="primary" @click="sendMessage($event)">发送</a-button>
        </span>
      </div>

    </footer>
    <setting-modal v-model:visible="state.visible" />
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
  border-top: 1px rgb(228, 228, 228) solid;
  width: 100%;
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
