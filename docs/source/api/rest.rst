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
            "id": "BTCB-USDT",
            "base": {
               "symbol": "BTCB",
               "address": "0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c",
               "decimals": 18,
               "native": false
            },
            "quote": {
               "symbol": "USDT",
               "address": "0x55d398326f99059fF775485246999027B3197955",
               "decimals": 18,
               "native": false
            },
            "price": 22905500000,
            "price_denom": 1000000,
            "reserve": 0,
            "reserve_denom": 1000000,
            "buffer": 1000,
            "buffer_denom": 1000000,
            "precision": 1,
            "txFee": "0.29",
            "timestamp": 1658380476654
            "minAmount": "500000000000000",
            "type": "major"
         }
         "timestamp": 1658380476712
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
   * **unwrap** (*number: 0 or 1*) -- Bid only option for native coins like BNB or ETH. Set to 1 to receive it in unwrapped native coins. 0 otherwise.


**Resquest**:
   .. sourcecode:: json
      
      {
         "order": {
            "account": "YOUR_ADDRESS",
            "tokenIn": "0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c",
            "tokenOut": "0x55d398326f99059fF775485246999027B3197955",
            "amout": "1500000000000000000", // 1.5 BTCB (decimals: 18)
            "lprice": "31500000000" // 31,500 usdt
         },
         "signature": "YOUR_SIGNATURE",
         "unwrap": "0"
      }


**Response**:
   .. sourcecode:: json

      {
         "code": 200,
         "reason": "Success",
         "result": true,
         "timestamp":1658380831967
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
         const domain = { name: 'oscillo', version: 'v1', chainId: 56, verifyingContract: '0x63c33e25051cf97312983f5e9624E00E7b4A424A' }	
         const types: Record<string, Array<TypedDataField>> = { Order: OrderTypeFields }	
         const signature = await wallet._signTypedData(domain, types, order)	
            
         const data = { order, signature, unwrap }	
         return axios({ method: 'POST', url: 'https://api-bsc.osc.finance/order', data })	
      }	

      const toLprice = (price: number, precision: number): number => parseFloat(price.toFixed(precision)) * 1_000_000	

      /**	
      * Sell 1.5 BTCB with lprice $31,500	
      *	
      * Market ID: BTCB-USDT	
      * Market Precision: 0	
      * Base Token: BTCB { address: 0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c, decimals: 18 }	
      * Quote Token: USDT { address: 0x55d398326f99059fF775485246999027B3197955, decimals: 18 }	
      * */	
      placeOrder('0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c', '0x55d398326f99059fF775485246999027B3197955', '1500000000000000000', toLprice(31500, 0), 0)	





Cancel Order
++++++++++++++++

.. http:delete::  /order 


:Parameters:

   * **cancel** (*object*)
            - account(*string*) -- User wallet address
            - key(*string*) --  OrderKey returned from placeOrder
   * **signature** (*string*) -- See `EIP-712 specification`_ , `SignTypedData`_ 
  

**Response**:
    .. sourcecode:: json

      {
         "code": 200,
         "reason": "Success",
         "result": true,
         "timestamp": 1658380476712
      }


.. code-block:: TypeScript
   :caption: *Cancel Order Sample*

      import axios from 'axios'
      import { ethers, Wallet } from 'ethers'
      import { TypedDataField } from '@ethersproject/abstract-signer'
      import { JsonRpcProvider } from '@ethersproject/providers'


      const CancelTypeFields = [
         { name: 'key', type: 'string' },
         { name: 'account', type: 'address' }
      ]

      const cancelOrder = async (key: string) => {
         const wallet: Wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', new JsonRpcProvider('YOUR_RPC_ENDPOINT'))
         const cancel = { account: wallet.address, key }         
         const domain = { name: 'oscillo', version: 'v1', chainId: 56, verifyingContract: '0x63c33e25051cf97312983f5e9624E00E7b4A424A' }
         const types: Record<string, Array<TypedDataField>> = { Cancel: CancelTypeFields }
         const signature = await wallet._signTypedData(domain, types, cancel)
         
         const data = { signature, cancel }
         return axios({ method: 'DELETE', url: 'https://api-bsc.osc.finance/order', data })
      }

      cancelOrder('YOUR_ORDER_KEY')



.. _Terminology: 
.. _EIP-712 specification: https://eips.ethereum.org/EIPS/eip-712
.. _SignTypedData: https://docs.ethers.io/v5/api/signer/#Signer-signTypedData
   