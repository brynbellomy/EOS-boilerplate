const EOS = require('eosjs')
const keystore = require('../keystore.json')

var eos

main()

async function main() {
    await initEOSJS()
    await doTransaction()
    await fetchResult()
}

async function initEOSJS() {
    const chainId = (await EOS().getInfo({})).chain_id
    eos = EOS({
        keyProvider: [ keystore.accounts['test.code'].activePrivateKey ],
        chainId,
    })

    // eos.getCurrencyBalance('eosio.token', 'eosio').then(x => console.log(x))
    // eos.getCurrencyStats()
}

async function doTransaction() {
    const pingContract = await eos.contract('test.code')
    const receipt = await pingContract.ping('test.code', {authorization: 'test.code@active'})
    console.log('Receipt:', receipt)
}

async function fetchResult() {
    let resp = await eos.getTableRows({
        json: true,
        code: 'test.code',
        table: 'player',
        scope: 'test.code', // this is the index to fetch
    })

    console.log('fetched ~>', resp)
}
