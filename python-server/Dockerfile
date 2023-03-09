# python 버전
FROM python:3.10.10

# 도커 이미지 내의 경로
WORKDIR /bonjin/app

#
COPY . .

RUN apt-get update
RUN apt-get -y install libqt5core5a
RUN apt-get -y install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
RUN apt-get -y install xvfb
RUN apt-get -y install wkhtmltopdf
RUN apt-get -y install fonts-liberation libasound2 libnspr4 libnss3 libu2f-udev xdg-utils
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libxrender1 \
        libfontconfig1 \
        libx11-dev \
        libqt5core5a \
        wget \
        unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome and chromedriver
RUN wget -N https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb \
    && wget -N https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && chmod +x chromedriver \
    && mv chromedriver /usr/local/bin \
    && rm -f chromedriver_linux64.zip \
    && rm -f google-chrome-stable_current_amd64.deb

# requirements.txt에 있는 패키지를 설치
RUN pip install -r requirements.txt

# Container 에 노출될 포트
EXPOSE 5000

CMD strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5

# app.py 실행
CMD python ./app.py 