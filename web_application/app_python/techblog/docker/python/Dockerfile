FROM python:latest

WORKDIR /usr/src/app

COPY ./docker/python/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]

# rubyをインストール(sassを使うために必要)
# ruby-devはgemでのエラー回避
RUN apt update && apt install -y ruby ruby-dev
RUN gem install sass
