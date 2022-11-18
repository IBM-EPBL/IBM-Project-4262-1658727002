FROM node:12
WORKDIR /app
COPY package*.json /app
RUN npm install

COPY . /app
COPY .env /app

EXPOSE 4500
CMD [ "npm", "run", "dev" ]
