#!/usr/bin/env bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 [Frp Version]"
    exit 1
fi

FRP_VERSION=$1
FRP_FILE_NAME="frp_${FRP_VERSION}_linux_amd64"
FRP_DOWNLOAD_URL_PREFIX='https://github.com/fatedier/frp/releases/download'
FRP_DOWNLOAD_URL="${FRP_DOWNLOAD_URL_PREFIX}/v${FRP_VERSION}/${FRP_FILE_NAME}.tar.gz"

TOKEN=$2
DASH_PASSWORD=$3

echo "Start make frp docker image version: ${FRP_VERSION}"

wget -O frp.tar.gz -T 30 $FRP_DOWNLOAD_URL
tar -xzf frp.tar.gz

rm -rf frp
mv $FRP_FILE_NAME frp
docker build -t frp:${FRP_VERSION} .

rm -rf frp*
echo "Build frp:${FRP_VERSION} docker image complete"

