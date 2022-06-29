***
FAQ
***

Why does oscillo use Index Price instead of AMM?
################################################
The key issue with using an AMM is that the execution price is never guaranteed, There is no MEV protection, and traders can lose part of their assets through slippage. Lastly, using an AMM is very cost inefficient for traders as this requires both a liquidity fee and a gas fee. Index price is an off-chain pricing strategy that uses the average market of various trusted sources to determine a specific market price. So oscillo doesn't require a liquidity fee and also can guarantee a profitable execution price without the risk of negative slippage or MEV attacks.


Always better than DEX? Is oscillo not a DEX?
#############################################
oscillo’s catchphrase is ‘Always better than DEX’. Sometimes people ask if oscillo is not a DEX. oscillo is definitely a decentralized exchange, but it is completely different from most of the traditional DEXs. Most DEXs rely on automated market makers (AMMs) to enable the swapping tokens, and although important, they’re far from perfect. AMMs are capital inefficient, prone to risks of MEV attacks, and cannot guarantee the execution price due to slippage. However oscillo’s peer-to-peer matchmaking protocol enables trading at the most profitable and guaranteed price. That’s why we say oscillo is ‘Always better than DEX’.


What is a trading fee?
################################
Trading fee is a protocol fee to execute transactions and the typical industry standard trading fee is about 0.1~0.5% of the transaction amount. However, oscillo’s trading fee will be waived until further notice to celebrate our launch. Also stablecoin pairs will remain with no trading fee.


What is a gasless transaction?
###############################
A third party(called a relayer) can send another user’s transactions and pay themselves for the gas cost. In this scheme, users sign messages(not transactions) containing information about a transaction they would like to execute. Relayers are then responsible for signing valid transactions with this information and sending them to the network, paying for the gas cost.


What is a settlement fee?
#########################
The settlement fee is the cost that is charged only when the order is completed. As oscillo uses off-chain pricing strategy, it doesn't require a gas fee for placing or canceling orders. This allows traders to save money on trades. However the settlement process must go through a smart contract to ensure a reliable transaction. In this process, oscillo pays the user’s gas fee on their behalf and deducts it from the user’s traded tokens. This means that users can trade despite not holding any native tokens(i.e. ETH on Ethereum network) Also, it helps to reduce transaction fee for large-scale traders who split trades into multiple transactions to avoid slippage. Because the settlement fee is only charged once even if an order is split by multiple participants.


What is MEV?
############
Maximal extractable value (MEV) refers to the maximum value that can be extracted from block production in excess of the standard block reward and gas fees by including, excluding, and changing the order of transactions in a block. Black hats can abuse these opportunities and attack a protocol.


How oscillo supports MEV-protection?
####################################
Trades in oscillo are simply token transfers that the buyer and seller both agreed on. The order of transactions in a block does not change the transfer amount, therefore, users are not at risk of MEV attacks.


How oscillo supports no slippage?
#################################
Unlike other DEXs, oscillo does not use liquidity pools of AMMs. Therefore, there is no slippage no matter the amount you desire to trade.


What is the Limit Price?
#####################
Limit price is the restriction on the maximum price to be paid or the minimum price to be received.


What is the Index Price?
#######################
Index price is an off-chain pricing system designed for the most profitable trading environment. Index price uses the average price of various trusted markets and trades on oscillo are only executed at index price when the index price satisfies or is more profitable than the limit price.


What is open order?
###################
It is a pending order that has not been matched yet.


Does oscillo support 'token-usdc' pairs only?
#############################################
Yes, for now you will only be able to buy tokens with USDC.


Why is my order split into multiple matches?
##############################################
Partial fills may occur when only a part of the order amount can be filled at or better than intended price, leaving an open order. This means that oscilo may complete your order by splitting it into multiple matches. Don’t worry about the fee, the settlement fee is only charged once even if an order is split by multiple participants.

oscillo prioritizes value over time. We believe that it is important to put users’ funds before the time it takes to complete an order. Often, the orders on other exchanges can't complete your order at the intended price, so you have to take unfavorable prices just to complete your order. oscillo believes that traders should not have to worry about what price they will receive their tokens. For this reason, trades on oscillo are only executed at index price when the index price satisfies or is more profitable than the trigger conditions.


Is oscillo a reliable protocol?
##################################
Sure, oscillo’s transaction goes through a reliable, non-upgradable smart contract. Also the source code of oscillo is disclosed transparently.

oscillo is a community built P2P trading protocol, initially developed for our own use. As we are also one of the users of oscillo, we're doing our best to keep the security and safety of oscillo. If you need a more clear answer on reliability, visit this `github <https://github.com/oscillo-finance>`_ and check it yourself.

Who made oscillo?
#################
We're a team of crypto traders and smart contract engineers. We've been working in DeFi since DeFi summer in 2020. 