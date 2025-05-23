FROM node:24-bullseye

WORKDIR /app
COPY package.json ./
COPY tsconfig.json ./

RUN npm install

COPY . .

ENV WDS_SOCKET_PORT=0

RUN npm run build
CMD ["npm", "start"]
