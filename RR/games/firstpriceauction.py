import random


# First Price Auction with Uniformly Distributed Valuations—Two PlayersA
class FirstPriceAuction:
    def __init__(self, n_players=2):
        assert n_players == 2, "Currently only supports 2 players."
        self.n_players = n_players
        self.valuations = [random.uniform(0, 1) for _ in range(n_players)]
        self.bids = [self.bidding_strategy(v) for v in self.valuations]

    def bidding_strategy(self, v):
        # BNE: b(v) = (n - 1)/n * v for uniform[0, 1]
        return 0.5 * v  # Only for 2 players

    def run_auction(self):
        winner = self.bids.index(max(self.bids))
        loser = 1 - winner
        payoffs = [0.0, 0.0]
        payoffs[winner] = self.valuations[winner] - self.bids[winner]
        return {
            "valuations": self.valuations,
            "bids": self.bids,
            "winner": winner,
            "payoffs": payoffs
        }

# Example usage
if __name__ == "__main__":
    game = FirstPriceAuction()
    result = game.run_auction()
    print(f"Valuations: {result['valuations']}")
    print(f"Bids: {result['bids']}")
    print(f"Winner: Player {result['winner']}")
    print(f"Payoffs: {result['payoffs']}")