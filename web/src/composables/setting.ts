import { useStorage } from '@vueuse/core'


type Setting = {
  app_key: string,
  model: string,
  continuously: boolean,
}

const setting = useStorage<Setting>('setting', {
  app_key: '',
  model: 'text-davinci-003',
  continuously: false,
})

const useSetting = () => setting

export default useSetting
