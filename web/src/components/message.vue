<script setup lang="ts">
import { message as messageTip } from 'ant-design-vue'
import { CopyOutlined } from '@ant-design/icons-vue'
import { useClipboard } from '@vueuse/core'

const { text, copy, copied, isSupported } = useClipboard({})
type Message = {
  msg: string;
  username: string;
  time: string;
  type: number;
}
defineProps<{
  message: Message;
}>()

const copyIt = (msg: string) => {
  copy(msg)
  messageTip.success('Copied')
}
</script>

<template>
  <div class="max-w-200" v-if="message.type === 1">
    <div class="p1-10 text-gray-400">
      <span class="pl-1 text-gray-800">{{ message.username }}</span>
      <span class="pl-3 text-gray-500">{{ message.time }}</span>
      <CopyOutlined class="pl-3 cursor-pointer" @click="copyIt(message.msg)" />
    </div>
    <div class="rounded-lg bg-blue-500 p-1 pl-3 text-light-50">
      <a-textarea class="a" :value="message.msg" autosize :bordered="false" />
    </div>
  </div>
  <div class="max-w-200" v-else>
    <div class="text-gray-400">
      <span class=" pl-1 text-gray-800">{{ message.username }}</span>
      <span class="pl-3 text-gray-500">{{ message.time }}</span>
      <CopyOutlined class="pl-3 cursor-pointer" @click="copyIt(message.msg)" />
      <div class="rounded-lg bg-gray-500 p-1 pl-3 text-white">
        <a-textarea class="b" :value="message.msg" autosize :bordered="false" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.ant-card-body {
  padding: 5px !important;
}

.a {
  width: 100%;
  color: white;
  background-color: rgba(59, 130, 246, var(--un-bg-opacity));
}

.b {
  width: 400px;
  color: white;
  background-color: rgba(107, 114, 128, var(--un-bg-opacity));
}
</style>
