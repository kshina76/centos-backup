FROM python:3.7.5-slim
RUN apt update
RUN apt -y install build-essential
RUN apt -y install wget
RUN pip install numpy
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
RUN tar -zxvf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib && \
  ./configure --prefix=/usr && \
  make && \
  make install && \
  cd .. && \
  rm -rf ta-lib-0.4.0-src.tar.gz && rm -rf ta-lib
RUN pip install TA-LIB
