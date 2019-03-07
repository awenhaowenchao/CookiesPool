FROM python:3.7-alpine3.8


WORKDIR /app

#安装需要的python库
#RUN apk update \
#    && apk upgrade \
RUN apk add bash \
    jpeg-dev zlib-dev \
    g++ \
    chromium chromium-chromedriver \
    libxml2 libxml2-dev libxslt-dev\
    && pip3 install --upgrade pip \
    && pip3 install requests \
    && pip3 install flask \
    && pip3 install redis \
    && pip3 install selenium \
    && pip3 install pillow \
    && pip3 install beautifulsoup4 \
    && pip3 install wheel \
    && pip3 install lxml \
    && mkdir -p /app/CookiesPool /app/CookiesPool/cookiespool /app/CookiesPool/login /app/CookiesPool/login/videorank /app/CookiesPool/login/wewen /app/CookiesPool/login/weibo /app/CookiesPool/login/weibo/templates /app/image
ADD ./cookiespool /app/CookiesPool/cookiespool
ADD ./login /app/CookiesPool/login
ADD ./login/videorank /app/CookiesPool/login/videorank
ADD ./login/weibo /app/CookiesPool/login/weibo
ADD ./login/weibo/templates /app/CookiesPool/login/weibo/templates
ADD ./login/wewen /app/CookiesPool/login/wewen

COPY . /app/CookiesPool
ENV PYTHONPATH=/app/CookiesPool:/usr/local/lib/python3.7/site-packages:$PYTHONPATH

CMD [ "python3", "/app/CookiesPool/run.py" ]

