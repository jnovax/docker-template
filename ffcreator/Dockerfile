FROM node:18-bookworm

LABEL author="hlam385@gmail.com"

RUN apt-get update
RUN apt-get -y install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++
RUN apt-get -y install libgl1-mesa-dev xvfb libxi-dev libx11-dev ffmpeg

WORKDIR /app
COPY . .
RUN npm i

ENTRYPOINT ["tail", "-f", "/dev/null"]