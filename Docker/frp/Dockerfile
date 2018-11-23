FROM alpine:3.6

COPY frp/frps /bin/frps
COPY entrypoint.sh /opt/frps/

RUN chmod +x /bin/frps && chmod +x /opt/frps/entrypoint.sh
WORKDIR /opt/frps/

ENV FRP_PORT=4000
ENV FRP_DASHBOARD=true
ENV FRP_DASHBOARD_PORT=4010
ENV FRP_DASHBOARD_USER frp_admin
ENV FRP_DASHBOARD_PWD frp_admin123

EXPOSE 4000-4010
ENTRYPOINT ["./entrypoint.sh"]
