REST API 
********


Rest API consists of market-side and order-side

* In Market-side: Retrive oscillo general information of markets
* In Order-side: Place Order and Cancel Order 

-----


Market
======

All Listing Markets Info
++++++++++++++++++++++++

.. http:get::  /market/


:Parameters:

   * **none**


**Response**:
   .. sourcecode:: json

     {
         "code": 200,
         "reason": "Success",
         "result": [
            {
               "base": {
                  "symbol": "WETH",
                  "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
                  "decimals": 18
               },
               "quote": {
                  "symbol": "USDC",
                  "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                  "decimals": 6
               },
               "price_denom": 1000000,
               "reserve": 0,
               "reserve_denom": 1000000,
               "market": "WETH-USDC",
               "minAmount": "30000000000000000",
               "price": 1784000000,
               "txFee": "22.5",
               "timestamp": 1654828501286
            },
            {
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
               "price_denom": 1000000,
               "reserve": 0,
               "reserve_denom": 1000000,
               "market": "WBTC-USDC",
               "minAmount": "250000",
               "price": 29967000000,
               "txFee": "22.5",
               "timestamp": 1654828501286
            },
            {
               "base": {
                  "symbol": "DAI",
                  "address": "0x6B175474E89094C44Da98b954EedeAC495271d0F",
                  "decimals": 18
               },
               "quote": {
                  "symbol": "USDC",
                  "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                  "decimals": 6
               },
               "price_denom": 1000000,
               "reserve": 0,
               "reserve_denom": 1000000,
               "market": "DAI-USDC",
               "minAmount": "40000000000000000000",
               "price": 999900,
               "txFee": "22.5",
               "timestamp": 1654828501286
            },
            {
               "base": {
                  "symbol": "USDT",
                  "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                  "decimals": 6
               },
               "quote": {
                  "symbol": "USDC",
                  "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
                  "decimals": 6
               },
               "price_denom": 1000000,
               "reserve": 0,
               "reserve_denom": 1000000,
               "market": "USDT-USDC",
               "minAmount": "40000000",
               "price": 999200,
               "txFee": "22.5",
               "timestamp": 1654828501286
            }
         ]
}


Specific Market Info
+++++++++++++++++++++

.. http:get::  /market/(string:market_id) 


:Parameters:

   * **market_id** (*string*) -- ``listing market id``.


**Response**:
   .. sourcecode:: json

      {
         "code": 200,
         "reason": "Success",
         "result": {
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
            "price_denom": 1000000,
            "reserve": 0,
            "reserve_denom": 1000000,
            "market": "WBTC-USDC",
            "minAmount": "250000",
            "price": 29963000000,
            "txFee": "22.5",
            "timestamp": 1654828480074
         }
      }



Order
=====


Place Order
++++++++++++++++

.. http:post::  /order 


:Parameters:

   * **order** (*object*) -- 
            - account(*string*): user wallet address
            - tokenIn(*string*): input token address
            - tokenOut(*string*): output token address
            - amount(*string*): trading amount(base token amount)
            - lprice(*number*): Guaranteed Price. Orders are traded at a favorable price than lprice. The lprice denominator is 1e6.

   * **signature** (*string*) -- Ref `EIP-712 specification`_ , `SignTypedData`_ 

   * **unwrap** (*number: 0 or 1*) -- Only for wrapped token bid order, would choose wrappred (0) or native (1). For example, Bid order of WMATIC-USDC market in Polygon Network or WETH-USDC market in Ethereum Network



.. note::
   
   :Terminology:
      .. figure:: static/lprice.png
         :align: center
         :figwidth: 100%

      * **lprice** -- the guaranteed price and is the worst price that can be accepted in the order request. For quick execution of orders, the lprice should be set at a disadvantage compared to the market price. When the market price of WBTC is $30,000, selling lprice should be less than $30,000, and buying lprice should be above $30,000. In the oscillo interface, lprice is displayed as only if [≥, ≤]

**Resquest**:
   .. sourcecode:: json
      
      // 1.5 WBTC ask order 
      {
         "order":{
            "account":"YOUR_ADDRESS",
            "tokenIn":"0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
            "tokenOut":"0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "amout":"150000000", // 1.5 WBTC (WBTC decimal: 8)
            "lprice":"31500000000" // 31,500 usdc
         },
         "signature":"signed signature",
         "unwrap":"0"
      }


**Response**:
   .. sourcecode:: json

      {
         "code":200,
         "reason":"Success",
         "result":"{order}:1" // OrderKey
      }


.. code-block:: TypeScript
   :caption: *Place Order Sample*

	
      import axios from 'axios'	
      import { ethers, Wallet } from 'ethers'	
      import { TypedDataField } from '@ethersproject/abstract-signer'	
      import { JsonRpcProvider } from '@ethersproject/providers'	
      const OrderTypeFields = [	
         { name: 'account', type: 'address' },	
         { name: 'tokenIn', type: 'address' },	
         { name: 'tokenOut', type: 'address' },	
         { name: 'amount', type: 'uint256' },	
         { name: 'lprice', type: 'uint256' }	
      ]	
      const placeOrder = async (tokenIn: string, tokenOut: string, amount: string, lprice: number, unwrap: number) => {	
         const wallet: Wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', new JsonRpcProvider('YOUR_RPC_ENDPOINT'))	
         const order = { account: wallet.address, tokenIn, tokenOut, amount, lprice }	
         const domain = { name: 'oscillo', version: 'v1', chainId: 1, verifyingContract: '0xCD2203534539Ac6b82d2D21B8575fe0F8Ca42Ccf' }	
         const types: Record<string, Array<TypedDataField>> = { Order: OrderTypeFields }	
         const signature = await wallet._signTypedData(domain, types, order)	
            
         const data = { order, signature, unwrap }	
         return axios({ method: 'POST', url: 'https://api-eth.osc.finance/order', data })	
      }	
      const toLprice = (price: number, precision: number): number => parseFloat(price.toFixed(precision)) * 1_000_000	
      /**	
      * Sell 1.5 WBTC with lprice $31,500	
      *	
      * Market ID: WBTC-USDC	
      * Market Precision: 0	
      * Base Token: WBTC { address: 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599, decimals: 8 }	
      * Quote Token: USDC { address: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48, decimals: 6 }	
      * */	
      placeOrder('0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599', '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', '150000000', toLprice(31500, 0), 0)	





Cancel Order
++++++++++++++++

.. http:delete::  /order 


:Parameters:

   * **account** (*string*) -- User Address.
   * **signature** (*string*) -- `EIP-712 specification`_ , `SignTypedData`_ 
   * **key** (*string*) -- orderKey



**Response**:
    .. sourcecode:: json

      {
         "code":200,
         "reason":"Success",
         "result":true
      }


.. code-block:: TypeScript
   :caption: *Cancel Order Sample*

      import axios from 'axios'
      import { ethers, Wallet } from 'ethers'
      import { TypedDataField } from '@ethersproject/abstract-signer'
      import { JsonRpcProvider } from '@ethersproject/providers'


      const CancelTypeFields = [{ name: 'key', type: 'string' }]

      const cancelOrder = async (key: string) => {
         const wallet: Wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', new JsonRpcProvider('YOUR_RPC_ENDPOINT'))
         
         const domain = { name: 'oscillo', version: 'v1', chainId: 1, verifyingContract: '0xCD2203534539Ac6b82d2D21B8575fe0F8Ca42Ccf' }
         const types: Record<string, Array<TypedDataField>> = { Cancel: CancelTypeFields }
         const signature = await wallet._signTypedData(domain, types, { key })
         
         const data = { key, signature: signature, account: wallet.address }
         return axios({ method: 'DELETE', url: 'https://api-eth.osc.finance/order', data })
      }

      cancelOrder('YOUR_ORDER_KEY')



.. _EIP-712 specification: https://eips.ethereum.org/EIPS/eip-712
.. _SignTypedData: https://docs.ethers.io/v5/api/signer/#Signer-signTypedData
   