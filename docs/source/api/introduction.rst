Introduction
************


| Documentation for Developers,
| by Developers

-----



.. _general_info:

General API Information
=======================

oscillo supports BNB Smart Chain(BSC) networks.


BSC
   - REST_API_ENDPOINT: https://api-bsc.osc.finance
   - WEBSOCKET_API_ENDPOINT: wss://api-bsc.osc.finance


All endpoints return either a JSON object or array.
All time and timestamp related fields are in milliseconds.




HTTP Return Codes
-----------------

- HTTP 4XX return codes are used for malformed requests; the issue is on the sender's side.
- HTTP 403 return code is used when the WAF Limit (Web Application Firewall) has been violated.
- HTTP 429 return code is used when breaking a request rate limit.
- HTTP 418 return code is used when an IP has been auto-banned for continuing to send requests after receiving 429 codes.
- HTTP 5XX return codes are used for internal errors; the issue is on oscillo internal server error.





Rate Limits
-----------

oscillo rate limiters defined about REST api calls.
When the api count exceeds the limit, you will receive a 429 error. Please check the following rate Limit rules.

===================== =========================== =======================
    RATE LIMIT             Duration(milliseconds)       Max Count
===================== =========================== =======================
    api Limiter            15 * 60 * 1000               1500
===================== =========================== =======================


WebSocket Heartbeat(ping/pong)
------------------------------

oscillo websocket's heartbeat interval is ``30_000 ms``, 
WS clients have to send the reponse(pong) to keep the connection alive or the connection will be broken.



.. _terminology:

Terminology
-----------

.. figure:: static/lprice.png
    :align: center
    :figwidth: 100%
    :width: 200px


* **price**: The market price of oscillo. All orders are traded at the market price.

* **price_denom**: 1e6.

* **precision**: The range of the floating-point of the ``price``. ``lprice`` is expressed as a combination of ``precision`` and ``price_denom``. lprice = price.toFixed(precision) * price_denom

* **lprice**: the guaranteed price and is the worst price that can be accepted in the order request. For quick execution of orders, the ``lprice`` should be set at a disadvantage compared to the market ``price``. When the market ``price`` of BTC is $30,000, selling ``lprice`` should be less than $30,000, and buying ``lprice`` should be above $30,000. In the oscillo interface, ``lprice`` is displayed as only if [≥, ≤]

* **reserve**: This is the protocol reserve of the market deducted from your token received. The reserves are redistributed to participants through OSC tokens. TradingFee = reserve / reserve_denome * TradeVolume

* **reserve_denom**: 1e6.

* **minAmount**: Minimum tradable amount. If the available order amount is less than minAmount, the order will be cancelled automatically.

* **txFee**: The gas cost of executors performing transactions on your behalf. It is deducted from your token received. Denominated in dollar value.

* **buffer**: The weight of lprice relative to index price. In auto-limit mode, ``lprice`` is determined [*buy order* = index price + index price * (buffer / buffer_denom), *sell order* = index price - index price * (buffer / buffer_denom)]

* **buffer_denom**: 1e6.



.. _contract:

Contract
========


oscillo contract
  ============================== ================================================= 
      .. centered:: Contract      .. centered:: Address                   
  ============================== =================================================
      .. centered:: Exchange       0xa1CAbab1D6E0007f721a20cf1ECBC9167Cd1404e
      .. centered:: OSCToken       0x7e00AecaBA5df64e9FeFAb55aC6B3F58100e79E2  
  ============================== ================================================= 




.. _listing:

Listing
=======

.. note::

  :In Market:
    * **Base Token**: Refers to the asset that is the quantity. For the BTC-USDT Market, BTC would be the base token.
    * **Quote Token**: Refers to the asset that is the price. For the BTC-USDT Market, USDT would be the quote token.


BSC
    ========================= ======================= ======================================================
    .. centered:: Market ID    .. centered:: Type       .. centered:: Base / Quote Token Address                     
    ========================= ======================= ======================================================
    .. centered:: BTC-USDT     .. centered:: MAJOR      | 0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c(BTC)/
                                                         0x55d398326f99059fF775485246999027B3197955(USDT)
    .. centered:: ETH-USDT     .. centered:: MAJOR      | 0x2170Ed0880ac9A755fd29B2688956BD959F933F8(ETH)/
                                                         0x55d398326f99059fF775485246999027B3197955(USDT)
    .. centered:: BNB-USDT     .. centered:: MAJOR      | 0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c(BNB)/
                                                         0x55d398326f99059fF775485246999027B3197955(USDT)  
    ========================= ======================= ======================================================


