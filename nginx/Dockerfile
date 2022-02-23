FROM nginx:1.21-alpine
RUN mkdir /game_nerd
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
WORKDIR /game_nerd