import random

class FirstPriceAuction:
    def __init__(self, n_bidders):
        if n_bidders < 2:
            raise ValueError("Auction requires at least two bidders.")
        self.n = n_bidders
        self.valuations = [random.uniform(0, 1) for _ in range(self.n)]
        self.bids = [self.bidding_strategy(v) for v in self.valuations]

    def bidding_strategy(self, valuation):
        return (self.n - 1) / self.n * valuation

    def run(self):
        highest_bid = max(self.bids)
        winners = [i for i, b in enumerate(self.bids) if b == highest_bid]
        winner = random.choice(winners)  # Break ties randomly

        payoffs = [0] * self.n
        payoffs[winner] = self.valuations[winner] - self.bids[winner]

        return {
            "valuations": self.valuations,
            "bids": self.bids,
            "winner": winner,
            "payoffs": payoffs
        }

if __name__ == "__main__":
    auction = FirstPriceAuction(n_bidders=5)
    result = auction.run()
    print("Valuations:", result["valuations"])
    print("Bids:", result["bids"])
    print(f"Winner: Player {result['winner']}")
    print("Payoffs:", result["payoffs"])