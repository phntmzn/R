import random

class FirstPriceAuctionNPlayers:
    def __init__(self, n_players):
        if n_players < 2:
            raise ValueError("Auction requires at least two players.")
        self.n_players = n_players
        self.valuations = [random.uniform(0, 1) for _ in range(n_players)]
        self.bids = [self.bidding_strategy(v) for v in self.valuations]

    def bidding_strategy(self, v):
        # BNE: b(v) = (n-1)/n * v for uniform[0, 1]
        return (self.n_players - 1) / self.n_players * v

    def run_auction(self):
        max_bid = max(self.bids)
        winners = [i for i, b in enumerate(self.bids) if b == max_bid]
        winner = random.choice(winners)  # tie-breaking at random
        payoffs = [0.0] * self.n_players
        payoffs[winner] = self.valuations[winner] - self.bids[winner]
        return {
            "valuations": self.valuations,
            "bids": self.bids,
            "winner": winner,
            "payoffs": payoffs
        }

# Example usage
if __name__ == "__main__":
    auction = FirstPriceAuctionNPlayers(n_players=5)
    result = auction.run_auction()
    print("Valuations:", result["valuations"])
    print("Bids:", result["bids"])
    print("Winner: Player", result["winner"])
    print("Payoffs:", result["payoffs"])