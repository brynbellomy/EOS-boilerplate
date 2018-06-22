import subprocess
import time
import json
import re

def createWallet(walletName=None, cleos='cleos'):
    cmd = [cleos, 'wallet', 'create']
    if walletName is not None:
        cmd += ['-n', walletName]

    output = getOutput(' '.join(cmd))
    match = re.search(r'"(PW[a-zA-Z0-9]+)"', output)
    walletPassword = match.group(1)
    # "/opt/eosio/bin/keosd" launched
    # Creating wallet: test
    # Save password to use in the future to unlock this wallet.
    # Without password imported keys will not be retrievable.
    # "PW5KJ..."
    return walletPassword

def createKey(cleos='cleos'):
    output = getOutput(cleos + ' create key')
    # Private key: 5JZVK...
    # Public key: EOS6WJ...
    privateKey = re.search(r'Private key: (.*)\n', output).group(1)
    publicKey  = re.search(r'Public key: (.*)\n', output).group(1)
    return privateKey, publicKey

def importKey(walletName, privateKey, cleos='cleos'):
    run(cleos + ' wallet import -n %s %s' % (walletName, privateKey))
    # imported private key for: EOS6WJ...

def createAccount(accountName, ownerPublicKey, activePublicKey, parentAccount='eosio', stakeNet=None, stakeCPU=None, buyRamKB=0, cleos='cleos'):
    # @@TODO: support other account creation command
    # cleos create account eosio $ACCOUNT_NAME $OWNER_PUBLIC_KEY $ACTIVE_PUBLIC_KEY
    # cleos system newaccount --stake-net '123 SYS' --stake-cpu '123 SYS' --buy-ram-kbytes 64 eosio test.code EOS7mPAZSSHQHvHntvgZa4mN1TRrWQE8J3mj65TG98b3WvkVDPohd

    cmd = [cleos, 'system', 'newaccount']
    if stakeNet is not None:
        cmd += ['--stake-net', "'" + stakeNet + "'"]
    if stakeCPU is not None:
        cmd += ['--stake-cpu', "'" + stakeCPU + "'"]
    if buyRamKB > 0:
        cmd += ['--buy-ram-kbytes', str(buyRamKB)]
    cmd += [parentAccount, accountName, ownerPublicKey, activePublicKey]
    run(' '.join(cmd))

def run(args):
    print('$', args)
    # logFile.write(args + '\n')
    if subprocess.call(args, shell=True):
        print('Exiting because of error')
        sys.exit(1)

def retry(args):
    while True:
        print('$', args)
        # logFile.write(args + '\n')
        if subprocess.call(args, shell=True):
            print('*** Retry')
        else:
            break

def background(args):
    print('$', args)
    # logFile.write(args + '\n')
    return subprocess.Popen(args, shell=True)

def getOutput(args):
    print('$', args)
    # logFile.write(args + '\n')
    proc = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE)
    return proc.communicate()[0].decode('utf-8')

def getJsonOutput(args):
    print('$', args)
    # logFile.write(args + '\n')
    proc = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE)
    return json.loads(proc.communicate()[0])

def sleep(t):
    print('sleep', t, '...')
    time.sleep(t)
    print('resume')
