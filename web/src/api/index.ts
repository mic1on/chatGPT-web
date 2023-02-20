import { getRequest, postRequest } from "./api";
import { useStorage } from '@vueuse/core'
const api_key = useStorage('api_key', '')

export const completion = async (text: string) => {
  const res = await postRequest({
    url: '/completions',
    data: {
      model: 'text-davinci-003',
      prompt: text,
      max_tokens: 2048,
      temperature: 0.9,
      frequency_penalty: 0,
      presence_penalty: 0,
      stop: [
        "\nAI:",
        "\nUser:",
    ]
    },
    headers: {
      api_key: api_key.value,
    }
  })
  return res
}

export const creditSummary = async () => {
  return await getRequest({
    url: '/credit_summary',
    headers: {
      api_key: api_key.value,
    }
  })
}
