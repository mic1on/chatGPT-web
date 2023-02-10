FROM registry.cn-hangzhou.aliyuncs.com/miclon/py-nodejs:latest

WORKDIR /app
# Install app dependencies
COPY . /app
RUN cd /app/web && pnpm install && pnpm run build
RUN cp -r /app/web/dist /app/api/dist
RUN cd /app/api && pip install -r requirements.txt

CMD ["/bin/bash", "start.sh"]