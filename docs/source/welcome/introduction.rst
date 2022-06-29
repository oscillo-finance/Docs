******************
Introduction
******************

Why did we build oscillo?
#########################

The cryptocurrency market experiences many ups and downs as it grows. These ups and downs give enormous trading opportunities for crypto-traders. Decentralized exchanges including AMMs also grow as crypto’s trading volume increases. However, AMMs have many defects, which always results in asset loss of some kind via slippage or impermanent loss. The process by which validators process transactions can also lead to unexpected asset loss through frontrunning, sandwiching, etc. Users have had to use unreasonable processes in an effort to reduce asset losses. We built oscillo to fix these problems and trade cheaper and safer.

----

What makes oscillo unique?
################

* **Index Price**: off-chain pricing system that uses the average price of various trusted markets.
* **Index-Limit Order**: only executed at index price when the index price satisfies or is more profitable than the trigger conditions.
* **Hybrid On/Off chain**: off-chain pricing for slippage or MEV protection and on-chain settlement for reliable transaction.

----

How does oscillo works?
#######################

Users create limit orders and sign the cryptographic signature in their wallet app as detailed in the `trading guide <https://docs.osc.finance/en/latest/quickstart/simple.html>`_. Once the user inputs a limit order, oscillo searches for a counterpart order matching the user’s trade conditions and matches are only executed at index price when the index price satisfies or is more profitable than the trigger conditions and then the order will be filled at the index price (more favorable prices can be generated if the index price is more profitable than the limit price). In order to make any changes to the order, it must be canceled and placed again. Users may cancel their order at any time before finding a match without incurring a penalty or gas fee.

----

What's the oscillo's benefit for traders?
##########################################

* **Guaranteed Price**: Trade any volume of tokens without losing money on price impact, slippage or MEV attacks.
* **Free Trading**: oscillo currently offers a zero trading fee promotion for all trading pairs to celebrate our launch.
* **Gasless(meta)**: The only thing you need to start trading is a gasless signature.
* **Decentralized**: Revenue generated from oscillo will be shared across all oscillo traders.

Guaranteed Price
****************
Since every AMM based exchange transaction affects the price of pooled assets, the price may appear to be different from that of other exchanges. As prices get out of sync, users’ orders may get executed at a more unfavorable price than intended. As oscillo uses the average price of various trusted markets, users will never get put into a situation where they have to trade with a more unfavorable price compared to other exchanges even if one of those markets drops below the standard. Furthermore, if you are trading an asset with low liquidity such as small cap coins, with orderbook based CEXs, a large order can cause price impact. Often, the exchange can't complete your order at the intended price, so you have to take unfavorable prices just to complete your order. Oscillo believes that traders should not have to worry about what price they will receive their tokens. For this reason, trades on oscillo are only executed at index price when the index price satisfies or is more profitable than the trigger conditions.

Free Trading
************
We are offering a zero trading fee promotion for all trading pairs. Most exchanges charge users fees at a certain percentage of a transaction amount. It means the higher the trading volume, the higher the trading fee becomes. So now oscillo is the best opportunity for both large and low scale traders. Note that oscillo plans to continue offering zero trading fee for USD stablecoin pairs even after the promotion.

Gasless(meta)
*************
Most decentralized exchanges use a smart contract to power all of their trades, which means that every time an order is placed, canceled, or filled, a gas fee is incurred which can make the process very expensive. Especially for lower scale traders, there are many cases where the fees are even greater than their order. However, from the user’s perspective, the oscillo’s exchanging operation will appear to be gasless, because oscillo uses off-chain pricing and on-chain settlement. When a user places an order, they must sign the transaction via their preferred wallet application. This process is gasless. When the user signs the transaction, they agree to send their order to oscillo to match and fill. In the settlement process that goes through a smart contract in order to ensure a reliable transaction, oscillo pays the user’s gas fee on their behalf and deducts it from the user’s traded tokens. This means that users can trade on oscillo despite not holding any native tokens(i.e. ETH on Ethereum network ). Also, oscillo helps large-scale traders drastically reduce transaction fees, as the settlement fee is charged only once even if an order is split by multiple participants.

Decentralized
*************
Reward system to be announced after closing the zero trading fee promotion. Stay tuned!

----

Roadmap | To-do list
############
We think these items are needed to trade reasonably in Defi. We will choose the top priority according to the traders' voices.

* Derivatives
* Multichain support
* Batch trade for stablecoins
* NFT trade
* Accounts for enterprises
* Combination trade
