FROM node:22.19.0

WORKDIR /app

COPY . /app

RUN npm cache clean --force
RUN npm install

EXPOSE 3000
CMD ["npm", "run", "dev"]
