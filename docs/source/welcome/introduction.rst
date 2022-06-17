******************
Introduction
******************

Why did we build oscillo?
#########################

The cryptocurrency market experiences many ups and downs as it grows. These ups and downs give enormous trading opportunities for crypto-traders. Decentralized exchanges including AMMs also grow as crypto’s trading volume increases. However, AMMs have many defects, which always results in asset loss of some kind via slippage or impermanent loss. The process by which validators process transactions can also lead to unexpected asset loss through frontrunning, sandwiching, etc. Users have had to use unreasonable processes in an effort to reduce asset losses. We built oscillo to fix these problems and trade cheaper and safer.

----

What is oscillo?
################

oscillo is a trading protocol with gasless transactions with an order book system similar to centralized exchanges. Traders are able to use gasless transactions to make limit orders. oscillo sends these transactions to the blockchain and pays the transaction fee. When using oscillo, traders do not have to provide native tokens such as ETH or MATIC for gas. Their assets remain in their wallet until the moment their order processes.

----

How does oscillo works?
#######################

#. A maker/taker creates an order
#. The order is hashed, and the maker/taker signs the order cryptographically.
#. The order is submitted to the order book.
#. oscillo matches the submitted orders.
#. oscillo verifies the maker/taker's digital signature and looks through all the conditions of the trade. If everything is correct, the assets will be transferred from the maker/taker wallets. If not, the transaction is canceled.

----

Key features
############

* **Fair price**: At DEXes, you unavoidably overpay and undersell tokens because of price impact and slippage. However, with oscillo, one  is able to buyfor the intended price.
* **Zero trading fee**: oscillo is built for all crypto traders. To celebrate the launch, trading fees will be waived until further notice. We will always be dedicated to keeping the lowest fees.
* **No slippage**: oscillo doesn't use liquidity pools like AMMs. Therefore, there is no slippage however the amount you trade.
* **Mev-resistance**: All trades in oscillo use the limit price at the time of order. Because the submitted price won’t change, oscillo isn’t susceptible to MEV attacks that would take advantage of arbitrary reorder transactions.

----

Roadmap | To-do list
####################
We think these items are needed to trade reasonably in Defi. We will choose the top priority according to the traders' voices.

* Derivatives
* Multichain support
* Batch trade for stablecoins
* NFT trade
* Accounts for enterprises
* Combination trade
