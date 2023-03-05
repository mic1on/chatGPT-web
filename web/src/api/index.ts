import { getRequest, postRequest } from "./api";
import useSetting from "@/composables/setting";
import { TSummary } from '@/types'

const setting = useSetting()
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
      api_key: setting.value.app_key,
    }
  })
  return res
}

export const completionTurbo = async (text: string) => {
  const res = await postRequest({
    url: '/completions_turbo',
    data: {
      model: 'gpt-3.5-turbo',
      messages: [{ "role": "user", "content": text }],
      stop: [
        "\nAI:",
        "\nUser:",
      ]
    },
    headers: {
      api_key: setting.value.app_key,
    }
  })
  return res
}

interface creditSummaryType {
  total_available: number;
  total_granted: number;
  total_used: number;
}

export const creditSummary = async (): Promise<creditSummaryType> => {
  return await getRequest({
    url: '/credit_summary',
    headers: {
      api_key: setting.value.app_key,
    }
  })
}
