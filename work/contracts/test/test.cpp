#include <eosiolib/eosio.hpp>

using namespace eosio;

class pingpong : public eosio::contract
{
  public:
    using contract::contract;

    /// @abi action
    void ping( account_name user ) {
         print( "Pong, ", name{user} );

         require_auth(user);

         playerIndex players(_self, _self);
         auto iterator = players.find(user);

         if (iterator == players.end()) {
             players.emplace(user, [&](auto& player) {
                player.username = user;
                player.level = 123;
            });
         } else {
             players.modify(iterator, user, [&](auto& player) {
                player.username = user;
                player.level++;
            });
         }
    }

    //@abi table player i64
    struct player {
        account_name username;
        uint64_t level;

        uint64_t primary_key() const { return username; }

        EOSLIB_SERIALIZE(player, (username)(level))
    };
    typedef multi_index<N(player), player> playerIndex;
};

EOSIO_ABI( pingpong, (ping) )