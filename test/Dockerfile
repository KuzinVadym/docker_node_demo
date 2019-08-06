FROM node:carbon

# Create app directory
WORKDIR /usr/src/test

# Install app dependencies
COPY package.json ./

# RUN npm install

# Bundle app source
COPY . /usr/src/test

EXPOSE 3333

CMD ["yarn", "start"]