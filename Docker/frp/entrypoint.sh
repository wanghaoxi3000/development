#!/usr/bin/env sh

CONFIG_FILE=./config/frps.ini

if [ ! -f ./config/frps.ini ]
then
    mkdir -p ./config

    if [ -n $FRP_TOKEN ]; then
        echo 'using /dev/random to create token'
        FRP_TOKEN=$(head -c 10 /dev/random | base64)
    fi

    echo "FRP TOKEN: $FRP_TOKEN"

    echo "[common]" > ${CONFIG_FILE}
    echo "bind_port = ${FRP_PORT}" >> ${CONFIG_FILE}
    echo "token = ${FRP_TOKEN}" >> ${CONFIG_FILE}

    if [ -n $FRP_DASHBOARD  ]; then
        echo "enable dashbard user: ${FRP_DASHBOARD_USER} password: ${FRP_DASHBOARD_PWD}"

        echo "dashboard_port = ${FRP_DASHBOARD_PORT}" >> ${CONFIG_FILE}
        echo "dashboard_user = ${FRP_DASHBOARD_USER}" >> ${CONFIG_FILE}
        echo "dashboard_pwd = ${FRP_DASHBOARD_PWD}" >> ${CONFIG_FILE}
    fi
fi

echo "run frp server"
frps -c ${CONFIG_FILE}
