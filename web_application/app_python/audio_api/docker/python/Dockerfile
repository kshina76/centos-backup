#FROM python:latest
FROM python:3.8

WORKDIR /usr/src/app

COPY ./docker/python/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/app"

# rubyをインストール(sassを使うために必要)
# ruby-devはgemでのエラー回避
RUN apt update && apt install -y ruby ruby-dev
RUN gem install sass
