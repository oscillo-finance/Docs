How does oscillo works?
=======================


1. A maker(bid)/taker(ask) creates an order
2. The order is hashed, and the maker/taker signs the order cryptographically.
3. The order is submitted to the order book.
4. oscillo matches each other's submitted orders.
5. oscillo verifies the maker/taker's digital signature and all conditions of trade. If so, the assets involved are swapped between maker and taker. If not, the trade is reverted.



