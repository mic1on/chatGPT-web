import { getRequest, postRequest } from "./api";
import useSetting from "@/composables/setting";
import { TSummary } from '@/types'

const setting = useSetting()
export const completion = async (model: string, text: string) => {
  const max_tokens_dict: { [key: string]: number } = {
    'text-davinci-003': 4097,
    'text-davinci-002': 4097,
    'text-curie-001': 2048,
    'text-babbage-001': 2048,
    'text-ada-001': 2048,
  }
  const res = await postRequest({
    url: '/completions',
    data: {
      model: model,
      prompt: text,
      max_tokens: max_tokens_dict[model] - text.length,
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
