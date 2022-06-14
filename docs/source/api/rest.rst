REST API 
********


Available REST endpoints ``market``, ``order``

* market -- Market information
* order -- Place or cancel order

-----


Market
======

Market Info
+++++++++++

.. http:get::  /market
.. http:get::  /market/(string:market_id) 


:Parameters:

   * **market_id** (*string*) -- Listed market id



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
            "price": 29963000000,
            "price_denom": 1000000,
            "reserve": 0,
            "reserve_denom": 1000000,
            "precision": 0,
            "market": "WBTC-USDC",
            "minAmount": "250000",
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

   * **order** (*object*)
            - account(*string*) -- User wallet address
            - tokenIn(*string*) -- Input token address
            - tokenOut(*string*) -- Output token address
            - amount(*string*) -- Trading amount (base token amount)
            - lprice(*number*) -- Guaranteed Price. Orders are traded at a favorable price than lprice. The lprice denominator is 1e6. See :ref:`Terminology <terminology>`
   * **signature** (*string*) -- See `EIP-712 specification`_ , `SignTypedData`_ 
   * **unwrap** (*number: 0 or 1*) -- Bid only option for native coins like ETH or MATIC. Set to 1 to receive it in unwrapped native coins. 0 otherwise.


**Resquest**:
   .. sourcecode:: json
      
      {
         "order": {
            "account": "YOUR_ADDRESS",
            "tokenIn": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
            "tokenOut": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
            "amout": "150000000", // 1.5 WBTC (decimals: 8)
            "lprice": "31500000000" // 31,500 usdc
         },
         "signature": "YOUR_SIGNATURE",
         "unwrap": "0"
      }


**Response**:
   .. sourcecode:: json

      {
         "code": 200,
         "reason": "Success",
         "result": "{order}:1" // OrderKey
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
         const domain = { name: 'oscillo', version: 'v1', chainId: 1, verifyingContract: '0x84B676e883d8Ee7Ca37160F2b21E0c5D6B81D0cA' }	
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

   * **account** (*string*) -- User wallet address
   * **signature** (*string*) -- See `EIP-712 specification`_ , `SignTypedData`_ 
   * **key** (*string*) -- OrderKey returned from placeOrder



**Response**:
    .. sourcecode:: json

      {
         "code": 200,
         "reason": "Success",
         "result": true
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
         
         const domain = { name: 'oscillo', version: 'v1', chainId: 1, verifyingContract: '0x84B676e883d8Ee7Ca37160F2b21E0c5D6B81D0cA' }
         const types: Record<string, Array<TypedDataField>> = { Cancel: CancelTypeFields }
         const signature = await wallet._signTypedData(domain, types, { key })
         
         const data = { key, signature: signature, account: wallet.address }
         return axios({ method: 'DELETE', url: 'https://api-eth.osc.finance/order', data })
      }

      cancelOrder('YOUR_ORDER_KEY')



.. _Terminology: 
.. _EIP-712 specification: https://eips.ethereum.org/EIPS/eip-712
.. _SignTypedData: https://docs.ethers.io/v5/api/signer/#Signer-signTypedData
   