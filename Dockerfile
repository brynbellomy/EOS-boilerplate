FROM eosio/eos-dev

COPY setup-network.py /setup/setup-network.py
COPY accounts.json /setup/accounts.json
COPY genesis.json /setup/genesis.json

