***
FAQ
***


oscillo is not a DEX?
#####################

Strictly speaking, oscillo is a kind of DEX. oscillo has the model that supports off-chain order book and on-chain settlement.
People usually come into their heads that DEX = AMM. so we use the catchphrase 'Always better than DEX' to express that oscillo is much better than AMMs.



Isn't this free? What is a transaction fee?
###########################################

oscillo sends the transaction on behalf of you. this is called gasless transaction(or meta-transaction). oscillo pays the gas fee first and requests for repaying this under the name of '**transaction fee**'.



What is MEV?
############

Maximal extractable value (MEV) refers to the maximum value that can be extracted from block production in excess of the standard block reward and gas fees by including, excluding, and changing the order of transactions in a block.
Someone can attack by abusing MEV opportunities.



How oscillo supports MEV-protection?
####################################

Trades in oscillo are just token transfers that the buyer and seller both agreed on. The order of transactions in a block doesn't change the transfer amount, so the buyer and seller are free from MEV.



How oscillo supports no slippage?
#################################

oscillo doesn't use liquidity pools of AMM. So there's no slippage however the amount you trade.



What is Limit-price(lprice)?
############################

Limit-price(lprice) is the guaranteed price and the worst price that can be an acceptable condition of the order. For quick execution of orders, your lprice should be set at a disadvantage compared to the market price. For example, when the market price of WBTC is $30,000, selling lprice should be less than $30,000, and buying lprice should be above $30,000. In oscillo interface, lprice is displayed as "only if [≥ or ≤ number]".


What is open order?
###################

It is the order pending to find its matches.


Does oscillo support 'token-usdc' pairs only?
#############################################

Yes, you can only buy tokens with USDC for a while.


I submitted an order just once, but why did the matches occur more than once?
#############################################################################

When my order amount isn't the same as the order amount of the other side, the matches can occur more than once. But the transaction fee will be charged only for the initial match, later matches are free.



Is oscillo safe?
################

This is a utility we made for ourselves, we are using this most. And we are disclosing all the code transparently on our Github(). So if you are a trader, please check our code and utilize this.



Who made oscillo?
#################

We are crypto traders. We made oscillo for trading cheaper without risk in the middle of arbitraging between DEX and CEX.