WEBSOCKET
*********

oscillo has 3 websocket channels [orderbook, order, market]

1. market: General Information of All Markets
2. orderbook: Price and Depth Size Data
3. order: Order Stream Data of target address
   
-----



Subscribe/Unsubscribe
=====================


Subscribe
+++++++++++

**Request**:
    .. sourcecode:: json

      {
         "type": "subscribe",
         "channel": "market",  // 'market' or 'orderbook' or 'order'
         "interest": "WBTC-USDC"  // 'market_id' for market and orderbook channels, 'user address' for order channel 
      }


**Response(market)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "subscribed",
         "channel": "market",
         "interest": "WBTC-USDC",
         "timestamp": 1654767820713,
         "contents": { // recent market data
            "base": {
               "symbol": "WBTC",
               "address": "0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6",
               "decimals": 8
            },
            "quote": {
               "symbol": "USDC",
               "address": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
               "decimals": 6
            },
            "price_denom": 1000000,
            "reserve": 1000,
            "reserve_denom": 1000000,
            "precision": 0,
            "market": "WBTC-USDC",
            "minAmount": "1000",
            "price": 30586000000,
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
         "contents": { // orderbook snapshot data
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
         "interest": "user address",
         "timestamp": 1654767820712,
         "contents": [  // order snapshot data
            {
               "key": "{order}:21",
               "account": "user address",
               "market": "dWBTC-dUSDC",
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
               "account": "user address",
               "market": "dWBTC-dUSDC",
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

**Request**:
    .. sourcecode:: json

      {
         "type": "unsubscribe",
         "channel": "market",  // 'market' or 'orderbook' or 'order'
         "interest": "WBTC-USDC"  // 'market_id' for market and orderbook channels, 'user address' for order channel 
      }

**Response**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "unsubscribed",
         "channel": "requested channel",  // 'market' or 'orderbook' or 'order'
         "interest": "requested interest",  // 'market_id' for market and orderbook channels, 'user address' for order channel 
         "timestamp": 1654767820714
      }


Market
======

publish message
+++++++++++++++

**Response(type: update)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "update", // only update
         "channel": "market",
         "interest": "WBTC-USDC",  // market-id
         "contents": {  // updated data
               "base": {
                  "symbol": "WBTC",
                  "address": "0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6",
                  "decimals": 8
               },
               "quote": {
                  "symbol": "USDC",
                  "address": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
                  "decimals": 6
               },
               "price_denom": 1000000,
               "reserve": 1000,
               "reserve_denom": 1000000,
               "precision": 0,
               "market": "WBTC-USDC",
               "minAmount": "1000",
               "price": 30986000000,
               "txFee": "0.0113",
               "timestamp": 1654767820709
         }
         "timestamp": 1654767820714
      }


Orderbook
=========

publish message
+++++++++++++++

**Response(type: update)**:
    .. sourcecode:: json

      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "update", // only update
         "channel": "orderbook",
         "interest": "WBTC-USDC",  // market-id
         "contents": {  // only changed data
              "asks": [
                 { "price": 30700000000, "size": "10000000" } 
               ]
         }
         "timestamp": 1654767820714
      }

Order
=====

publish message
+++++++++++++++

**Response(type: add|remove|update)**:
    .. sourcecode:: json

      // type: add  
      // condition: User created new order
      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "add",
         "channel": "order",
         "interest": "user address",  // user address-id
         "contents": [ // removed order info
            {
               "key": "{order}:21",
               "account": "user address",
               "market": "dWBTC-dUSDC",
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
      // condition: order was matched or recover 
      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "remove",
         "channel": "order",
         "interest": "user address",  // user address-id
         "contents": [ // updated order info
            {
               "key": "{order}:21",
               "account": "user address",
               "market": "dWBTC-dUSDC",
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
      // condition: new order was created
      {
         "connection_id": "07b03b90-463e-4d4c-989e-8c2763d4ebb1",
         "type": "update",
         "channel": "order",
         "interest": "user address",  // user address-id
         "contents": [ // created order info
            {
               "key": "{order}:21",
               "account": "user address",
               "market": "dWBTC-dUSDC",
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