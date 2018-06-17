var EOS = require('eosjs')

var eos = EOS()

// eos.getBlock({ block_num_or_id: 1 }).then(console.log)
// console.log(eos)
eos.getCurrencyBalance('eosio.token', 'eosio').then(x => console.log(x))
// eos.getCurrencyStats()
// eos.getProducers({lower_bound: 0}).then(console.log)