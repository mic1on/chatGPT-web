<script setup lang="ts">
import { message as messageTip } from 'ant-design-vue'
import { Viewer } from '@bytemd/vue-next'
import highlight from '@bytemd/plugin-highlight'
import 'highlight.js/styles/atom-one-light.css'
import useMessages from '@/composables/messages'
import { CopyOutlined, DeleteOutlined } from '@ant-design/icons-vue'
import { useClipboard } from '@vueuse/core'
import { TMessage } from '@/types'


const messages = useMessages()
const { copy } = useClipboard({})
defineProps<{
  message: TMessage;
}>()

const copyIt = (msg: string) => {
  copy(msg)
  messageTip.success('Copied')
}

const deleteIt = (meseage: TMessage) => {
  messages.messages.value = messages.messages.value.filter((item) => item !== meseage)
  messageTip.success('Deleted')
}
</script>

<template>
  <div class="my-2 self-end flex items-center flex-row" v-if="message.type === 1">
    <DeleteOutlined class="pr-1 cursor-pointer self-end !text-gray-400" @click="deleteIt(message)" />
    <div class="p-1 rounded-t-lg rounded-l-lg bg-blue-300 shadow text-sm min-w-10 max-w-500">
      <!-- <pre class="max-w-80 !mb-0 m-2">{{ message.msg }}</pre> -->
      <Viewer class="max-w-120 m-2" :value="message.msg" :plugins="[highlight()]" />
    </div>
  </div>
  <div class="my-2 self-start flex items-center" v-else>
    <div class="p-1 rounded-t-lg rounded-r-lg bg-gray-100 text-black shadow text-sm min-w-10">
      <!-- <pre class="max-w-80 !mb-0">{{ message.msg }}</pre> -->
      <Viewer class="max-w-120 m-2" :value="message.msg" :plugins="[highlight()]" />
    </div>
    <CopyOutlined class="pl-2 cursor-pointer self-end !text-gray-400" @click="copyIt(message.msg)" />
    <DeleteOutlined class="pl-1 cursor-pointer self-end !text-gray-400" @click="deleteIt(message)" />
  </div>
</template>

<style scoped>
.ant-card-body {
  padding: 5px !important;
}

.a {
  color: black;
  background-color: white;
}

.b {
  color: white;
  background-color: rgba(96, 165, 250, var(--un-bg-opacity));
}

p {
  margin-bottom: 0 !important;
}
</style>
