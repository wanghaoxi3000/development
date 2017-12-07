FROM ubuntu:14.04
MAINTAINER wanghaoxi3000 <wanghaoxi3000@163.com>

RUN apt-get update && apt-get install -y --no-install-recommends \
    python-pip git wget build-essential && \
    apt-get clean

RUN wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz \
    && tar zxf LATEST.tar.gz \
    && cd libsodium* \
    && ./configure && make && make install \
    && ldconfig && make distclean

RUN pip install git+https://github.com/shadowsocks/shadowsocks.git@master

ENTRYPOINT ["/usr/local/bin/ssserver"]
