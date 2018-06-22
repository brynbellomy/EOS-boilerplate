#!/usr/bin/python3

import json
from util import run, retry, background, getOutput, getJsonOutput, createKey, importKey, createAccount, createWallet

walletName = 'test'
accountName = 'test.code'

print('Creating wallet...')
walletPassword = createWallet(walletName=walletName)

print('Creating owner key...')
ownerPrivateKey, ownerPublicKey = createKey()

print('Importing owner key...')
importKey(walletName, ownerPrivateKey)

print('Creating active key...')
activePrivateKey, activePublicKey = createKey()

print('Importing active key...')
importKey(walletName, activePrivateKey)

print('Creating account...')
createAccount(accountName, ownerPublicKey, activePublicKey, parentAccount='eosio', stakeNet='123 SYS', stakeCPU='123 SYS', buyRamKB=64)

with open('/work/keystore.json', 'r+') as f:
    keystore = {}
    try:
        keystore = json.load(f)
    except:
        pass

    keystore['wallets'] = keystore.get('wallets', {})
    keystore['accounts'] = keystore.get('accounts', {})
    keystore['wallets'][walletName] = {
        'name': walletName,
        'password': walletPassword,
    }
    keystore['accounts'][accountName] = {
        'name': accountName,
        'parentAccount': parentAccount,
        'ownerPublicKey': ownerPublicKey,
        'ownerPrivateKey': ownerPrivateKey,
        'activePublicKey': activePublicKey,
        'activePrivateKey': activePrivateKey,
    }
    json.dump(keystore, f)

print('Wallet/account info saved to ./keystore.json')

