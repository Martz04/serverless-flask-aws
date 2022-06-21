FROM node:18-alpine3.15

RUN apk update \
    && apk add -q python3 \
    curl

WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm install -g serverless

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py

COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN mkdir ~/.aws
COPY src .

EXPOSE 8080

CMD [ "python3", "./src/app.py"]