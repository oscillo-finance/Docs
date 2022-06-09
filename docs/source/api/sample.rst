SAMPLE CODE
*************

   REST & WS API Implement
   
-----



TypeScript
===========


.. code-block:: TypeScript
   :caption: *oscillo api sample*

    class Oscillo {
    private static _instance: Oscillo
    readonly emitter = new EventEmitter()
    private _wallet: Wallet
    private _ws: WebSocket
    private _heartbeatTimer: NodeJS.Timer
    
    private _markets: Record<string, Market> = {}
    private _orderbooks: Record<string, Orderbook> = {}
    private _orders: Order[] = []
    
    static instance() {
        if (!this._instance) {
            this._instance = new Oscillo()
        }
        
        this._instance._wallet = new ethers.Wallet(PK, new JsonRpcProvider(PROVIDER_ENDPOINT))
        this._instance.initialize()
        return this._instance
    }
    
    private constructor() {
    }
    
    /** WebSocket **/
    
    private initialize() {
        if (this._heartbeatTimer) clearInterval(this._heartbeatTimer)
        this._heartbeatTimer = setInterval(() => this.heartbeat(), 5000)
        
        this._ws = new WebSocket(OSC.POLYGON.WSS_ENDPOINT)
        
        this._ws.on('open', async () => console.log('Connection Established!'))
        this._ws.on('ping', () => this._ws.pong())
        this._ws.on('message', rawData => this.handleMessage(rawData))
        this._ws.once('error', () => this._ws.close())
        this._ws.once('close', () => setTimeout(() => this.initialize(), 3000))
        
    }
    
    private heartbeat() {
        if (!this._ws || this._ws.readyState !== WebSocket.OPEN) {
            this.initialize()
            return
        }
        this._ws.ping()
    }
    
    /**
     * Subscribe
     * @params
     * channel: SocketChannel [order, orderbook, market]
     * interest: order => wallet address /  orderbook & market => marketId
     * type: [subscribe, unsubscribe]
     * **/
    subscribe(channel: SocketChannel, interest: string, type = 'subscribe') {
        if (!this._ws) return
        if (this._ws && this._ws.readyState === WebSocket.CONNECTING) {
            setTimeout(() => this.subscribe(channel, interest, type), 3000)
            return
        }
        
        this._ws.send(JSON.stringify({ type, channel, interest }))
    }
    
    private handleMessage(rawData: WebSocket.RawData) {
        const parsed = JSON.parse(rawData.toString())
        switch (parsed.channel) {
            case SocketChannel.market:
                this._markets[parsed.interest] = parsed.contents
                break
            case SocketChannel.orderbook:
                this.parseOrderbook(parsed.type, parsed.interest, parsed.contents)
                break
            case SocketChannel.order:
                this.parseOrder(parsed.type, parsed.contents)
                break
        }
    }
    
    private parseOrderbook(type: SocketResponseType, interest: string, contents: Orderbook) {
        switch (type) {
            case SocketResponseType.subscribed:
                this._orderbooks[interest] = contents
                break
            case SocketResponseType.unsubscribed:
                delete this._orderbooks[interest]
                break
            default:
                const asks = this._orderbooks[interest].asks || []
                const bids = this._orderbooks[interest].bids || []
                
                const askRemovedPrices = (contents.asks || []).filter(each => BigNumber.from(each.size).isZero()).map(each => each.price)
                const askUpdatedDepths = (contents.asks || []).filter(each => !BigNumber.from(each.size).isZero())
                askUpdatedDepths.forEach((depth: Depth) => {
                    const idx = asks.findIndex(each => each.price === depth.price)
                    if (idx < 0) asks.push(depth)
                    else asks[idx] = depth
                })
                
                const bidRemovedPrices = (contents.bids || []).filter(each => BigNumber.from(each.size).isZero()).map(each => each.price)
                const bidUpdatedDepths = (contents.bids || []).filter(each => !BigNumber.from(each.size).isZero())
                bidUpdatedDepths.forEach((depth: Depth) => {
                    const idx = bids.findIndex(each => each.price === depth.price)
                    if (idx < 0) bids.push(depth)
                    else bids[idx] = depth
                })
                
                this._orderbooks[interest] = {
                    asks: sortBy(asks.filter(each => !askRemovedPrices.includes(each.price)), 'price'),
                    bids: sortBy(bids.filter(each => !bidRemovedPrices.includes(each.price)), 'price')
                }
                break
        }
    }
    
    private parseOrder(type: SocketResponseType, contents: Order[]) {
        switch (type) {
            case SocketResponseType.subscribed:
                this._orders = contents
                break
            case SocketResponseType.unsubscribed:
                this._orders = []
                break
            case SocketResponseType.add:
                this._orders = [...contents, ...this._orders]
                break
            case SocketResponseType.remove:
                this._orders = this._orders.filter(each => !contents.map(removed => removed.key).includes(each.key))
                break
            case SocketResponseType.update:
                this._orders = this._orders.map(each => contents.find(updated => updated.key === each.key) ?? each).filter(each => each.status !== OrderStatus.Filled)
                contents.map(v => this.emitter.emit(v.key, v))
                break
        }
    }
    
    /** Rest **/
    
    async placeOrder(tokenIn: string, tokenOut: string, amount: string, lPrice: number, unwrap: number = 0) {
        const order = { account: this._wallet.address, tokenIn: tokenIn, tokenOut: tokenOut, amount: amount, lprice: lPrice.toFixed() }
        const domain = { name: 'Oscillo', version: 'v1', chainId: OSC.POLYGON.CHAIN_ID, verifyingContract: OSC.POLYGON.EXCHANGE_ADDRESS }
        const types: Record<string, Array<TypedDataField>> = { Order: OrderTypeFields }
        const signature = await this._wallet._signTypedData(domain, types, order)
        
        const data = { order: order, signature: signature, unwarp: unwrap }
        return axios({ method: 'POST', url: `${OSC.POLYGON.REST_ENDPOINT}/order`, data })
    }
    
    async cancelOrder(key: string) {
        const domain = { name: 'Oscillo', version: 'v1', chainId: OSC.POLYGON.CHAIN_ID, verifyingContract: OSC.POLYGON.EXCHANGE_ADDRESS }
        const types: Record<string, Array<TypedDataField>> = { Cancel: CancelTypeFields }
        const signature = await this._wallet._signTypedData(domain, types, { key })
        const data = { key, signature: signature, account: this._wallet.address }
        
        return axios({ method: 'DELETE', url: `${OSC.POLYGON.REST_ENDPOINT}/order`, data })
    }

    

