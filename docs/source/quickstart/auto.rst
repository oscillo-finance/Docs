Trade with an auto-limit mode
========================

.. role:: raw-html(raw)
    :format: html;

Interface
---------

Here's the trading interface

.. figure:: static/auto_limit.png
    :align: center
    :figwidth: 100%

a. Token selection
b. These two numbers mean buy(bid, green) side token and sell(ask, red) side token.
c. Simple mode to expert mode or vice versa
d. Where you input the desired amount of selected token to trade. Minimum amount may change depending on gas fee.
e. Your wallet balance
f. Latest price of selected token
g. Hourly price change of selected token

Step
----

1. Click 'Connect Wallet' and choose a preferred wallet.

.. figure:: static/before_connection.png
    :align: center
    :figwidth: 100%

:raw-html:`<br />`

- We currently support Metamask, Trust Wallet, Math Wallet, and WalletConnect.

.. figure:: static/choose_wallet.png
    :align: center
    :figwidth: 100%

:raw-html:`<br />`

2. Click '▼' to select token.

.. figure:: static/click_arrow.png
    :align: center
    :figwidth: 100%

:raw-html:`<br />`

.. figure:: static/choose_token.png
    :align: center
    :figwidth: 100%

:raw-html:`<br />`

3.  Enter your desired amount of selected token and click the 'BUY' or 'SELL' button.

4.  Check your trigger condition and fees.

    * Keep the ordered amount in your wallet or order will be canceled.

    * Gas fee is paid by the executors performing transactions on your behalf. This fee will be automatically deducted from the tokens you receive from buying or selling.

.. figure:: static/sell_wbtc.png
    :align: center
    :figwidth: 100%

:raw-html:`<br />`

5. You will receive a signature request from 'osc.finance' in the wallet app. After confirming it, you will be able to see your order on the open order list.



