FROM node:lts-alpine as builder
WORKDIR /app

COPY ./src/webui/package*.json ./
RUN npm install
COPY ./src/webui .
RUN npm run build

# Production stage
FROM nginx:stable-alpine as production-stage

COPY --from=builder /app/dist /usr/share/nginx/html

COPY dockerfiles/prod/webui/nginx.conf /etc/nginx/
CMD ["nginx", "-g", "daemon off;"]

