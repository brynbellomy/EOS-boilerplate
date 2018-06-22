const EOS = require('eosjs')
const keystore = require('../keystore.json')

async function main() {
    const chainId = (await EOS().getInfo({})).chain_id
    const eos = EOS({
        keyProvider: [ keystore.accounts['test.code'].activePrivateKey ],
        chainId,
    })

    eos.getCurrencyBalance('eosio.token', 'eosio').then(x => console.log(x))
    // eos.getCurrencyStats()

    const pingContract = await eos.contract('test.code')
    const receipt = await pingContract.ping('blah', {authorization: 'test.code@active'})
    console.log('Receipt:', receipt)

}

main()