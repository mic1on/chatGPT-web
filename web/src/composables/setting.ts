import { useStorage } from "@vueuse/core";

type Setting = {
  app_key: string;
  base_url: string;
  model: string;
  continuously: boolean;
};

const setting = useStorage<Setting>("setting", {
  app_key: "",
  base_url: "",
  model: "gpt-3.5-turbo",
  continuously: false,
});

const useSetting = () => setting;

export default useSetting;
