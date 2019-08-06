FROM node:carbon

RUN npm install babel-cli@6.10.1 -g --save
RUN mkdir -p /usr/src/api
# Create app directory
WORKDIR /usr/src/api

# Install app dependencies
COPY package.json /usr/src/pi

# RUN npm install

# Bundle app source
COPY . /usr/src/api

ENV PORT=3000 MODE=prod

EXPOSE 3000

CMD ["npm", "run", "start"]