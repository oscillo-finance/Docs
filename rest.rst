REST API 
********


oscillo Rest API consists of market-side and order-side

In Market-side: Retrive oscillo Price History of listing market
In Order-side: Place Order and Cancel Order 

-----


Market
======


Price history
++++++++++++++++

.. http:get::  /api/market/(string:market_id)/prices 


:Parameters:

   * **market_id** (*string*) -- ``listing market id``.


**Response**:
   .. sourcecode:: json

      {
         "code":200,
         "reason":"Success",
         "result":[{"price":29902733300,"timestamp":1654153200000}]
      }


Order
=====


Place Order
++++++++++++++++

.. http:post::  /api/order 


:Parameters:

   * **order** (*object*) -- 
            - account(*string*): user wallet address
            - tokenIn(*string*): input token address
            - tokenOut(*string*): output token address
            - amount(*string*): trading amount base token amount
            - lprice(*number*): Minimum Guaranteed Price

   * **signature** (*string*) -- `EIP-712 specification`_

   * **unwrap** (*number: 0 or 1*) -- Only for wrapped token bid order, would choose wrappred (0) or native (1). For example, Bid order of WMATIC-USDC market in Polygon Network or WETH-USDC market in Ethereum Network


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

.. http:delete::  /api/order 


:Parameters:

   * **account** (*string*) -- User Address.
   * **signature** (*string*) -- `EIP-712 specification`_
   * **key** (*string*) -- orderKey



**Example response**:
    .. sourcecode:: json

      {
         "code":200,
         "reason":"Success",
         "result":true
      }


.. code-block:: TypeScript
   :caption: *Cancel Order Sample*

   const CancelTypeFields = [{ name: 'key', type: 'string' }]
   /**
    * CancelOrder
    */
    async cancelOrder(key: string) {
        const domain = { name: 'oscillo', version: 'v1', chainId: OSC.POLYGON.CHAIN_ID, verifyingContract: OSC.POLYGON.EXCHANGE_ADDRESS }
        const types: Record<string, Array<TypedDataField>> = { Cancel: CancelTypeFields }
        const signature = await this._wallet._signTypedData(domain, types, { key })
        const data = { key, signature: signature, account: this._wallet.address }
        
        return axios({ method: 'DELETE', url: `${OSC.POLYGON.REST_ENDPOINT}/order`, data })
    }


.. _EIP-712 specification: https://docs.ethers.io/v5/api/signer/#Signer-signTypedData
   