class StockPrice:

    def __init__(self):
        self.latest_time = 0
        self.time_price = dict()
        self.price_frequency = collections.Counter()

        self.mn_heap = []
        self.mx_heap = []

    def update(self, timestamp: int, price: int) -> None:
        # Get the previous price before updating
        old_price = self.time_price.get(timestamp, None)

        # Decrement the old price since it will be unused
        if old_price is not None:
            self.price_frequency[old_price] -= 1

        # Update the frequency of our new updated price
        self.price_frequency[price] += 1
        self.time_price[timestamp] = price
        heappush(self.mx_heap, -price)
        heappush(self.mn_heap, price)

        # Track the latest time
        self.latest_time = max(self.latest_time, timestamp)

    def current(self) -> int:
        return self.time_price[self.latest_time]

    # O(1) ammortized 
    def maximum(self) -> int:
        # This price is outdated, pop it off.
        while self.price_frequency[-self.mx_heap[0]] == 0:
            heappop(self.mx_heap)
        
        return -self.mx_heap[0]

    # O(1) ammortized
    def minimum(self) -> int:
        # This price is outdated, pop it off.
        while self.price_frequency[self.mn_heap[0]] == 0:
            heappop(self.mn_heap)
        
        return self.mn_heap[0]
        
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()