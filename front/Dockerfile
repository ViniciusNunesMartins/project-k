FROM node:16-alpine


RUN yarn add global http-server


WORKDIR /code


COPY package.json .
COPY yarn.lock .
COPY . .

RUN yarn



RUN yarn run build