# Imagem de Origem
FROM node:14-alpine

WORKDIR /code

COPY package.json .
COPY yarn.lock .

RUN yarn --silent

COPY . .