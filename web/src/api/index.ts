import { getRequest, postRequest } from "./api";

export const completion = async (text: string) => {
  const res = await postRequest({
    url: '/completions',
    data: {
      model: 'text-davinci-003',
      prompt: text,
      max_tokens: 2048,
      temperature: 0.5,
      frequency_penalty: 0,
      presence_penalty: 0,
      top_p: 1,
    }
  })
  return res
}

export const creditSummary = async () => {
  return await getRequest({
    url: '/credit_summary',
  })
}
