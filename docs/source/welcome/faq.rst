***
FAQ
***


Is oscillo not a DEX?
#####################

oscillo is a DEX. However, oscillo has a model that supports off-chain order books and on-chain settlement.
The belief that a DEX = an AMM is ingrained in many people’s heads. DEX = AMM. Therefore, we use the catchphrase "Always better than DEX" to express that oscillo is much better than AMMs.


Isn't this free? What is a settlement fee?
###########################################

Unlike other DEXes, oscillo pays for the transaction on your behalf. oscillo sends the transaction on behalf of you. This is called a gasless transaction(or meta-transaction). oscillo pays the gas fee first and so, the “Settlement fee” refers to the user’s repayment of this gas fee to oscillo.


What is a trading fee?
################################

Trading fee is the protocol fee. But this is free until further notice. Stablecoin pairs are always free.


What is a gasless transaction?
###############################

A third party(called a relayer) can send another user’s transactions and pay themselves for the gas cost. In this scheme, users sign messages(not transactions) containing information about a transaction they would like to execute. Relayers are then responsible for signing valid transactions with this information and sending them to the network, paying for the gas cost.


What is MEV?
############

Maximal extractable value (MEV) refers to the maximum value that can be extracted from block production in excess of the standard block reward and gas fees by including, excluding, and changing the order of transactions in a block.
Black hats can abuse these opportunities and attack a protocol.


How oscillo supports MEV-protection?
####################################

Trades in oscillo are simply token transfers that the buyer and seller both agreed on. The order of transactions in a block does not change the transfer amount, therefore, users are not at risk of MEV attacks


How oscillo supports no slippage?
#################################

Unlike other DEXes, oscillo does not  use liquidity pools of AMMs. Therefore, there is  no slippage no matter the amount you desire to trade.


What is Limit-price(lprice)?
############################

Limit-price(lprice) is the minimum price at which the token will be sold or bought. Your lprice should be set at a disadvantage compared to the market price. For example, when the market price of WBTC is $30,000, selling lprice should be less than $30,000, and buying lprice should be above $30,000. In oscillo’s interface, lprice is displayed as "only if [≥ or ≤ number]".


What is open order?
###################

It is a pending order not has been matched yet.


Does oscillo support 'token-usdc' pairs only?
#############################################

Yes, for now you will only be able to buy tokens with USDC.


I submitted an order just once, but why did the matches occur more than once?
#############################################################################

If the buying amount does not match the selling amount, matches must occur more than once in order to fulfill your entire order, and vice versa. However, the gas fee will only be charged for the initial match, later matches are free.


Is oscillo safe?
################

oscillo is a utility we made for all crypto traders, including ourselves. It is a protocol that we will also use and be invested in. Therefore, the safety of oscillo is of utmost importance to us.
All of our code is disclosed transparently on our Github. And our contracts are non-upgradable. So if you are a trader, please feel free to check our code and confirm for yourself.


Who made oscillo?
#################

We're a team of crypto traders and smart contract engineers. We've been working in DeFi since DeFi summer in 2020. 
