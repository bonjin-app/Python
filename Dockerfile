# python 버전
FROM python:3.10.10

# 도커 이미지 내의 경로
WORKDIR /bonjin/app

#
COPY . .

RUN apt-get update
RUN apt-get install wkhtmltopdf

# requirements.txt에 있는 패키지를 설치
RUN pip install -r requirements.txt

# Container 에 노출될 포트
EXPOSE 5000

# app.py 실행
CMD python ./app.py 