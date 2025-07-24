import itertools
import numpy as np

class NormalFormGame:
    def __init__(self, players, strategies, payoffs):
        """
        players: list of player names or indices
        strategies: dict {player: [list of pure strategies]}
        payoffs: dict {strategy_profile_tuple: (payoff1, payoff2, ..., payoffN)}
        """
        self.players = players
        self.strategies = strategies
        self.payoffs = payoffs
        self.n = len(players)

    def get_profiles(self):
        """Generate all pure strategy profiles."""
        strategy_lists = [self.strategies[player] for player in self.players]
        return list(itertools.product(*strategy_lists))

    def get_payoff(self, profile, player_index):
        """Return player i's payoff from the given strategy profile."""
        return self.payoffs[profile][player_index]

    def best_responses(self, fixed_profile, player_index):
        """Return best response(s) for player_index given others' strategies."""
        others = [s for i, s in enumerate(fixed_profile) if i != player_index]
        candidate_strats = self.strategies[self.players[player_index]]
        payoffs = []
        for s in candidate_strats:
            full_profile = list(others)
            full_profile.insert(player_index, s)
            payoff = self.get_payoff(tuple(full_profile), player_index)
            payoffs.append((s, payoff))
        max_payoff = max(p for s, p in payoffs)
        return [s for s, p in payoffs if np.isclose(p, max_payoff)]

    def is_nash_equilibrium(self, profile):
        """Check if a pure strategy profile is a Nash equilibrium."""
        for i in range(self.n):
            current_strategy = profile[i]
            br = self.best_responses(profile, i)
            if current_strategy not in br:
                return False
        return True

    def find_pure_nash_equilibria(self):
        """Return all pure strategy Nash equilibria."""
        return [profile for profile in self.get_profiles() if self.is_nash_equilibrium(profile)]
    
if __name__ == "__main__":
    players = ["P1", "P2"]
    strategies = {
        "P1": ["H", "T"],
        "P2": ["H", "T"]
    }
    payoffs = {
        ("H", "H"): (1, -1),
        ("H", "T"): (-1, 1),
        ("T", "H"): (-1, 1),
        ("T", "T"): (1, -1)
    }

    game = NormalFormGame(players, strategies, payoffs)
    print("Pure Nash Equilibria:", game.find_pure_nash_equilibria())