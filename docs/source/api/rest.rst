REST API 
********


Oscillo Rest API consists of market-side and order-side

In Market-side: Retrive Oscillo Price History of listing market.
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

   const OrderTypeFields = [
      { name: 'account', type: 'address' },
      { name: 'tokenIn', type: 'address' },
      { name: 'tokenOut', type: 'address' },
      { name: 'amount', type: 'uint256' },
      { name: 'lprice', type: 'uint256' }
   ]
   /**
    * PlaceOrder
    */
    async placeOrder(tokenIn: string, tokenOut: string, amount: string, lPrice: number, unwrap: number = 0) {
        const order = { account: this._wallet.address, tokenIn: tokenIn, tokenOut: tokenOut, amount: amount, lprice: lPrice.toFixed() }
        const domain = { name: 'Oscillo', version: 'v1', chainId: OSC.POLYGON.CHAIN_ID, verifyingContract: OSC.POLYGON.EXCHANGE_ADDRESS }
        const types: Record<string, Array<TypedDataField>> = { Order: OrderTypeFields }
        const signature = await this._wallet._signTypedData(domain, types, order)
        
        const data = { order: order, signature: signature, unwarp: unwrap }
        return axios({ method: 'POST', url: `${OSC.POLYGON.REST_ENDPOINT}/order`, data })
    }






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
        const domain = { name: 'Oscillo', version: 'v1', chainId: OSC.POLYGON.CHAIN_ID, verifyingContract: OSC.POLYGON.EXCHANGE_ADDRESS }
        const types: Record<string, Array<TypedDataField>> = { Cancel: CancelTypeFields }
        const signature = await this._wallet._signTypedData(domain, types, { key })
        const data = { key, signature: signature, account: this._wallet.address }
        
        return axios({ method: 'DELETE', url: `${OSC.POLYGON.REST_ENDPOINT}/order`, data })
    }


.. _EIP-712 specification: https://docs.ethers.io/v5/api/signer/#Signer-signTypedData
   