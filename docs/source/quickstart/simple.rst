Trade with a simple mode
========================

.. role:: raw-html(raw)
    :format: html;

Interface
---------

Here's the trading interface

.. figure:: static/simple_part.png
    :align: center
    :figwidth: 100%

a. You can choose the token you trade.
b. These two numbers mean buy(bid, green) side token and sell(ask, red) side token.
c. You can switch the mode from simple to expert.
d. This is the input area of the amount you trade. A minimum amount may be changed because of the gas fee.
e. This is your wallet balance.
f. This is the latest price of the token.
g. This graph shows the hourly price change.

Step
----

1. Click 'Connect Wallet' and choose the wallet you use.

.. figure:: static/before_wallet_connect.png
    :align: center
    :figwidth: 100%

:raw-html:`<br />`

- We currently support Metamask, Trust Wallet, Math Wallet, and Walletconnect.

.. figure:: static/choose_wallet.png
    :align: center
    :figwidth: 100%

:raw-html:`<br />`

2. Click '▼' to choose the token you trade.

.. figure:: static/dwbtc_click.png
    :align: center
    :figwidth: 100%

:raw-html:`<br />`

- dWBTC, dWETH, and dUSDC are just testing tokens with no value.

.. figure:: static/choose_token.png
    :align: center
    :figwidth: 100%

:raw-html:`<br />`

3.  Enter the amount you trade and click the 'BUY' or 'SELL' button.

4.  Check your trigger condition and transaction fee.

    * You should keep the amount you order in your wallet or your order will be canceled.

    * The transaction fee is the gas fee. This fee will be subtracted from the token you will receive automatically.

.. image:: static/buy.png
    :width: 49%

.. image:: static/sell.png
    :width: 49%

:raw-html:`<br />`

5. You receive the signature request from 'osc.finance' at the wallet app. After confirming it, your order will be seen on the open order list.



