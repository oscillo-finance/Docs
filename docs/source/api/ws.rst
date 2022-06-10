WEBSOCKET
*********


Available websocket channels ``market``, ``orderbook``, ``order``, 

* market -- Market information
* orderbook -- Price and depth size
* order -- Order data
   
-----



Subscribe/Unsubscribe
=====================


Subscribe
+++++++++++


:Parameters:

   * **type** (*string*) -- subscribe
   * **channel** (*string*) -- One of ``market``, ``orderbook``, ``order``
   * **interest** (*string*) -- MarketID for market and orderbook subscription, Wallet Address for order subscription


**Request**:
    .. sourcecode:: json

      {
         "type": "subscribe",
         "channel": "market",
         "interest": "WBTC-USDC"
      }


**Response(market)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "subscribed",
         "channel": "market",
         "interest": "WBTC-USDC",
         "timestamp": 1654767820713,
         "contents": {
            "base": {
               "symbol": "WBTC",
               "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
               "decimals": 8
            },
            "quote": {
               "symbol": "USDC",
               "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
               "decimals": 6
            },
            "price": 30586000000,
            "price_denom": 1000000,
            "reserve": 1000,
            "reserve_denom": 1000000,
            "precision": 0,
            "market": "WBTC-USDC",
            "minAmount": "1000",
            "txFee": "0.0113",
            "timestamp": 1654767820709
         }
      }



**Response(orderbook)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "subscribed",
         "channel": "orderbook",
         "interest": "WBTC-USDC",
         "timestamp": 1654767820714,
         "contents": {
            "asks": [ 
               { "price": 30700000000, "size": "50000000" },
               { "price": 30600000000, "size": "100000000" },
               { "price": 30500000000, "size": "70000000" },
            ],
            "bids": [
               { "price": 30435000000, "size": "50000000" },
               { "price": 30428000000, "size": "100000000" },
               { "price": 30358000000, "size": "70000000" }
         }
      }



**Response(order)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "subscribed",
         "channel": "order",
         "interest": "YOUR_ADDRESS",
         "timestamp": 1654767820712,
         "contents": [
            {
               "key": "{order}:21",
               "account": "YOUR_ADDRESS",
               "market": "WBTC-USDC",
               "side": 20,
               "lprice": 30285000000,
               "status": 1,
               "amount": "200000000",
               "filled": "0",
               "pending": "0",
               "unwrap": 0
            },
            {
               "key": "{order}:13",
               "account": "YOUR_ADDRESS",
               "market": "WBTC-USDC",
               "side": 20,
               "lprice": 30332000000,
               "status": 1,
               "amount": "100000000",
               "filled": "0",
               "pending": "0",
               "unwrap": 0
            }
         ]
      }

Unsubscribe
+++++++++++++


:Parameters:

   * **type** (*string*): unsubscribe
   * **channel** (*string*): One of ``market``, ``orderbook``, ``order``
   * **interest** (*string*): MarketID for market and orderbook subscription, Wallet Address for order subscription



**Request**:
    .. sourcecode:: json

      {
         "type": "unsubscribe",
         "channel": "market",
         "interest": "WBTC-USDC"
      }

**Response**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "unsubscribed",
         "channel": "market",
         "interest": "WBTC-USDC",
         "timestamp": 1654767820714
      }


Market
======

Payload
+++++++

**Response(type: update)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "update", // update only
         "channel": "market",
         "interest": "WBTC-USDC",
         "contents": {
               "base":{
                  "symbol":"WBTC",
                  "address":"0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
                  "decimals":8
               },
               "quote":{
                  "symbol":"USDC",
                  "address":"0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                  "decimals":6
               },
               "price":30986000000,
               "price_denom":1000000,
               "reserve":1000,
               "reserve_denom":1000000,
               "precision": 0,
               "market":"WBTC-USDC",
               "minAmount":"1000",
               "txFee":"0.0113",
               "timestamp":1654767820709
         }
         "timestamp": 1654767820714
      }


Orderbook
=========

Payload
+++++++

**Response(type: update)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "update", // update only
         "channel": "orderbook",
         "interest": "WBTC-USDC",
         "contents": {
              "asks": [{ "price": 30700000000, "size": "10000000" }] // size 0 for removal
         }
         "timestamp": 1654767820714
      }

Order
=====

Payload
+++++++

**Response(type: add|remove|update)**:
    .. sourcecode:: json

      // type: add  
      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "add",
         "channel": "order",
         "interest": "user address",
         "contents": [
            {
               "key": "{order}:21",
               "account": "user address",
               "market": "WBTC-USDC",
               "side": 20,
               "lprice": 30285000000,
               "status": 1,
               "amount": "200000000",
               "filled": "0",
               "pending": "0",
               "unwrap": 0
            }
         ]
         "timestamp": 1654767820714
      }

      // type: remove  
      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "remove",
         "channel": "order",
         "interest": "user address",
         "contents": [
            {
               "key": "{order}:21",
               "account": "user address",
               "market": "WBTC-USDC",
               "side": 20,
               "lprice": 30285000000,
               "status": 1,
               "amount": "200000000",
               "filled": "0",
               "pending": "0",
               "unwrap": 0
            }
         ]
         "timestamp": 1654767820714
      }

      // type: update
      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "update",
         "channel": "order",
         "interest": "user address",
         "contents": [
            {
               "key": "{order}:21",
               "account": "user address",
               "market": "WBTC-USDC",
               "side": 20,
               "lprice": 30285000000,
               "status": 1,
               "amount": "200000000",
               "filled": "0",
               "pending": "0",
               "unwrap": 0
            }
         ]
         "timestamp": 1654767820714
      }
