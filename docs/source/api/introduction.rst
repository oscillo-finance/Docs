Introduction
************


| Documentation for Developers,
| by Developers

-----



.. _general_info:

General API Information
=======================

oscillo supports two networks [ETHEREUM, POLYGON].



ETHEREUM
   - REST_API_ENDPOINT: https://api-eth.osc.finance
   - WEBSOCKET_API_ENDPOINT: wss://api-eth.osc.finance

POLYGON
   - REST_API_ENDPOINT: https://api-matic.osc.finance
   - WEBSOCKET_API_ENDPOINT: wss://api-matic.osc.finance


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

* **lprice**: the guaranteed price and is the worst price that can be accepted in the order request. For quick execution of orders, the ``lprice`` should be set at a disadvantage compared to the market ``price``. When the market ``price`` of WBTC is $30,000, selling ``lprice`` should be less than $30,000, and buying ``lprice`` should be above $30,000. In the oscillo interface, ``lprice`` is displayed as only if [≥, ≤]

* **reserve**: This is the protocol reserve of the market deducted from your token received. The reserves are redistributed to participants through OSC tokens. TradingFee = reserve / reserve_denome * TradeVolume

* **reserve_denom**: 1e6.

* **minAmount**: Minimum tradable amount. If the available order amount is less than minAmount, the order will be cancelled automatically.

* **txFee**: The gas cost of executors performing transactions on your behalf. It is deducted from your token received. Denominated in dollar value.





.. _contract:

Contract
========


oscillo contract
  ============================== ================================================= 
      .. centered:: Contract      .. centered:: Address                   
  ============================== =================================================
      .. centered:: Exchange       0xBB0Cb9007ceF526cEdEc48FDc6D5f750641244f0
      .. centered:: OSCToken       0x7e00AecaBA5df64e9FeFAb55aC6B3F58100e79E2  
      .. centered:: Distributor    0x3103683332086a746835655F656141cD5582a008         
  ============================== ================================================= 




.. _listing:

Listing
=======

.. note::

  :In Market:
    * **Base Token**: Refers to the asset that is the quantity. For the WBTC-USDC Market, WBTC would be the base token.
    * **Quote Token**: Refers to the asset that is the price. For the WBTC-USDC Market, USDC would be the quote token.


Ethereum
    ========================= ==========================================
    .. centered:: Market ID   .. centered:: Base / Quote Token Address                      
    ========================= ==========================================
    .. centered:: WBTC-USDC     | 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599(WBTC)/
                                  0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48(USDC)
    .. centered:: WETH-USDC     | 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2(WETH)/
                                 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48(USDC)
    .. centered:: DAI-USDC      | 0x6B175474E89094C44Da98b954EedeAC495271d0F(DAI)/
                                 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48(USDC)
    .. centered:: USDT-USDC     | 0xdAC17F958D2ee523a2206206994597C13D831ec7(USDT)/
                                 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48(USDC)
    ========================= ==========================================


Polygon
    ========================= ==========================================
    .. centered:: Market ID    .. centered:: Base / Quote Token Address                     
    ========================= ==========================================
    .. centered:: WBTC-USDC     | 0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6(WBTC)/
                                  0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174(USDC)
    .. centered:: WETH-USDC     | 0x7ceb23fd6bc0add59e62ac25578270cff1b9f619(WETH)/
                                  0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174(USDC)
    .. centered:: WMATIC-USDC   | 0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270(WMATIC)/
                                  0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174(USDC)
    .. centered:: DAI-USDC      | 0x8f3Cf7ad23Cd3CaDbD9735AFf958023239c6A063(DAI)/
                                  0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174(USDC)
    .. centered:: USDT-USDC     | 0xc2132d05d31c914a87c6611c10748aeb04b58e8f(USDT)/
                                  0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174(USDC)
    ========================= ==========================================

