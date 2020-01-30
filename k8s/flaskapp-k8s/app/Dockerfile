# ベースイメージ
FROM python:3.6

RUN mkdir /var/www
# workdirの指定
WORKDIR /var/www

#requirements.txtやその他のファイルをコピーする
ADD . .

# 依存Pythonライブラリインストール
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /var/www/src

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
