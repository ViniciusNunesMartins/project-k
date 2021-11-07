FROM node:16-alpine

WORKDIR /code

COPY package.json .
COPY yarn.lock .
COPY . .

RUN yarn
RUN yarn run build