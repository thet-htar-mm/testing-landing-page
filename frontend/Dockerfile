FROM node:22.19.0

WORKDIR /app

COPY . /app

RUN npm install

EXPOSE 3000
CMD ["npm", "run", "dev", "--host", "0.0.0.0", "--port", "3000"]
#CMD ["npm", "run", "dev"]
