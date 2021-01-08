FROM postgres:latest
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
#ENV LANG ja_JP.utf8
ENV LANG en_US.UTF-8
#COPY ./project/data/*.sql /docker-entrypoint-initdb.d/
