FROM registry.cn-hangzhou.aliyuncs.com/miclon/py-nodejs:latest as build
WORKDIR /app
COPY . /app
RUN cd /app/web && pnpm install && pnpm run build

FROM python:3.11-slim
WORKDIR /app
COPY api/requirements.txt /app/api/requirements.txt
RUN pip install --no-cache-dir -r api/requirements.txt
COPY --from=build /app/web/dist /app/api/dist
COPY start.sh /app
COPY api /app/api
CMD ["/bin/bash", "start.sh"]
