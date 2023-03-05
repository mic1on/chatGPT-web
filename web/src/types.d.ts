export type TMessage = {
  username: string
  msg: string
  type: number
  time?: string
}



export type TSummary = {
  total_available: number
  total_granted: number
  total_used: number
  [key: string]: any
}
