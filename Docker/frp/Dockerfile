FROM alpine:3.5

COPY frp/frpc /frpc
COPY frp/frps /frps
COPY frp/frpc.ini /frpc.ini
COPY frp/frps.ini /frps.ini

WORKDIR /

EXPOSE 80 443 6000 7000 7500

ENTRYPOINT ["/frps"]
