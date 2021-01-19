FROM kaggle/python:latest
# RUN apt update すでに入っている
# RUN apt -y install build-essential すでに入っている
# RUN apt -y install wget すでに入っている
COPY ./requirements.txt ./
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
RUN tar -zxvf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib && \
  ./configure --prefix=/usr && \
  make && \
  make install && \
  cd .. && \
  rm -rf ta-lib-0.4.0-src.tar.gz && rm -rf ta-lib
RUN pip install --no-cache-dir -r requirements.txt
