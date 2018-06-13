#!/bin/sh
sudo docker run --rm \
    --name eosio \
    -d \
    -p 8888:8888 \
    -p 9876:9876 \
    -v $PWD/work:/work \
    -v $PWD/chain:/mnt/dev/data \
    eosio/eos-dev \
    /bin/bash -c "nodeos -e -p eosio --plugin eosio::wallet_api_plugin --plugin eosio::wallet_plugin --plugin eosio::producer_plugin --plugin eosio::history_plugin --plugin eosio::chain_api_plugin --plugin eosio::history_api_plugin --plugin eosio::http_plugin -d /mnt/dev/data --http-server-address=0.0.0.0:8888 --access-control-allow-origin=* --contracts-console"

