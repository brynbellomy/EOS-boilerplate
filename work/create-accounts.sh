#!/bin/sh
set -e

WALLET_NAME=test
ACCOUNT_NAME=test.code

echo Creating wallet...
OUTPUT_WALLET_CREATE=$(cleos wallet create -n $WALLET_NAME)
WALLET_PASSWORD=$(echo "${OUTPUT_WALLET_CREATE}" | sed -n '4p' | sed 's/\"//g')
# "/opt/eosio/bin/keosd" launched
# Creating wallet: test
# Save password to use in the future to unlock this wallet.
# Without password imported keys will not be retrievable.
# "PW5KJ..."

echo Creating owner key...
OUTPUT_CREATE_KEY=$(cleos create key)
OWNER_PRIVATE_KEY=$( echo "${OUTPUT_CREATE_KEY}" | sed -n '1p' | awk '{print $NF}' )
OWNER_PUBLIC_KEY=$( echo "${OUTPUT_CREATE_KEY}" | sed -n '2p' | awk '{print $NF}' )
# Private key: 5JZVK...
# Public key: EOS6WJ...

echo Importing owner key...
cleos wallet import -n $WALLET_NAME $OWNER_PRIVATE_KEY
# imported private key for: EOS6WJ...

echo Creating active key...
OUTPUT_CREATE_KEY=$(cleos create key)
ACTIVE_PRIVATE_KEY=$( echo "${OUTPUT_CREATE_KEY}" | sed -n '1p' | awk '{print $NF}' )
ACTIVE_PUBLIC_KEY=$( echo "${OUTPUT_CREATE_KEY}" | sed -n '2p' | awk '{print $NF}' )
# Private key: 5JHBD...
# Public key: EOS8RA...

echo Importing active key...
cleos wallet import -n $WALLET_NAME $ACTIVE_PRIVATE_KEY
# imported private key for: EOS8RA...

echo Creating account...
# cleos create account eosio $ACCOUNT_NAME $OWNER_PUBLIC_KEY $ACTIVE_PUBLIC_KEY
cleos system newaccount --stake-net '123 SYS' --stake-cpu '123 SYS' --buy-ram-kbytes 32768 eosio $ACCOUNT_NAME $OWNER_PUBLIC_KEY $ACTIVE_PUBLIC_KEY
# cleos system newaccount --stake-net '123 SYS' --stake-cpu '123 SYS' --buy-ram-kbytes 64 eosio test.code EOS7mPAZSSHQHvHntvgZa4mN1TRrWQE8J3mj65TG98b3WvkVDPohd

echo Wallet name: $WALLET_NAME >> ./wallet-info.txt
echo Wallet password: $WALLET_PASSWORD >> ./wallet-info.txt
echo Account name: $ACCOUNT_NAME >> ./wallet-info.txt
echo Owner pubkey: $OWNER_PUBLIC_KEY >> ./wallet-info.txt
echo Active pubkey: $ACTIVE_PUBLIC_KEY >> ./wallet-info.txt

echo Wallet/account info saved to ./wallet-info.txt

