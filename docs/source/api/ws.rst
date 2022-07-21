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
         "interest": "WBTC-USDT"
      }


**Response(market)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "subscribed",
         "channel": "market",
         "interest": "WBTC-USDT",
         "timestamp": 1654767820713,
         "contents": {
            "id": "WBTC-USDT",
            "base": {
               "symbol": "WBTC",
               "address": "0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c",
               "decimals": 18,
               "native": false,
            },
            "quote": {
               "symbol": "USDT",
               "address": "0x55d398326f99059fF775485246999027B3197955",
               "decimals": 18,
               "native": false,
            },
            "price": 30586000000,
            "price_denom": 1000000,
            "reserve": 0,
            "reserve_denom": 1000000,
            "buffer":1000,
            "buffer_denom":1000000,
            "precision": 1,
            "txFee": "0.29",
            "timestamp": 1654767820709,
            "minAmount": "500000000000000",
            "type":"major"
         }
      }



**Response(orderbook)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "subscribed",
         "channel": "orderbook",
         "interest": "WBTC-USDT",
         "timestamp": 1654767820714,
         "contents": {
            "asks": [ 
               { "price": 30700000000, "size": "500000000000000" },
               { "price": 30600000000, "size": "1100000000000000" },
               { "price": 30500000000, "size": "500000000000000" },
            ],
            "bids": [
               { "price": 30435000000, "size": "500000000000000" },
               { "price": 30428000000, "size": "1100000000000000" },
               { "price": 30358000000, "size": "500000000000000" }
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
               "market": "WBTC-USDT",
               "side": 20,
               "lprice": 30285000000,
               "status": 1,
               "amount": "1000000000000000000",
               "filled": "0",
               "pending": "0",
               "unwrap": 0
            },
            {
               "key": "{order}:13",
               "account": "YOUR_ADDRESS",
               "market": "WBTC-USDT",
               "side": 20,
               "lprice": 30332000000,
               "status": 1,
               "amount": "2000000000000000000",
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
         "interest": "WBTC-USDT"
      }

**Response**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "unsubscribed",
         "channel": "market",
         "interest": "WBTC-USDT",
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
         "interest": "WBTC-USDT",
         "contents": {
               "base":{
                  "symbol": "WBTC",
                  "address": "0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c",
                  "decimals": 18,
                  "native": false
               },
               "quote":{
                  "symbol": "USDT",
                  "address": "0x55d398326f99059fF775485246999027B3197955",
                  "decimals": 18,
                  "native": false
               },
               "price": 30986000000,
               "price_denom": 1000000,
               "reserve": 0,
               "reserve_denom": 1000000,
               "buffer": 1000,
               "buffer_denom": 1000000,
               "precision": 1,
               "market": "WBTC-USDT",
               "minAmount": "500000000000000",
               "txFee": "0.29",
               "timestamp": 1654767820709,
               "type": "major"
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
         "interest": "WBTC-USDT",
         "contents": {
              "asks": [{ "price": 30700000000, "size": "1000000000000000000" }] // size 0 for removal
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
               "market": "WBTC-USDT",
               "side": 20,
               "lprice": 30285000000,
               "status": 1,
               "amount": "1000000000000000000",
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
               "market": "WBTC-USDT",
               "side": 20,
               "lprice": 30285000000,
               "status": 1,
               "amount": "1000000000000000000",
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
               "market": "WBTC-USDT",
               "side": 20,
               "lprice": 30285000000,
               "status": 1,
               "amount": "1000000000000000000",
               "filled": "0",
               "pending": "0",
               "unwrap": 0
            }
         ]
         "timestamp": 1654767820714
      }
