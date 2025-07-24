

class JobMarketSignalingGame:
    def __init__(self):
        self.types = ['high', 'low']           # Worker types
        self.education_cost = {'high': 1, 'low': 3}  # Cost of education
        self.wages = {'edu': 5, 'no_edu': 2}    # Firm's wage offer
        self.prior = {'high': 0.5, 'low': 0.5}  # Belief about types

    def separating_equilibrium(self):
        """
        In separating: High-type gets education, low-type doesn’t.
        Firm offers:
            - w_edu = 5 if edu
            - w_no_edu = 2 if no edu
        """
        decisions = {'high': 'edu', 'low': 'no_edu'}
        payoffs = {}
        for t in self.types:
            action = decisions[t]
            wage = self.wages[action]
            cost = self.education_cost[t] if action == 'edu' else 0
            payoffs[t] = wage - cost

        incentive_compatible = (
            payoffs['high'] >= self.wages['no_edu'] and
            payoffs['low'] >= self.wages['edu'] - self.education_cost['low']
        )
        return incentive_compatible, decisions, payoffs

    def pooling_equilibrium(self):
        """
        In pooling: Both types get education.
        Firm pays: w_edu = E[θ] based on priors (expected productivity)
        """
        expected_productivity = (
            self.prior['high'] * 5 + self.prior['low'] * 2
        )
        payoffs = {}
        for t in self.types:
            cost = self.education_cost[t]
            payoffs[t] = expected_productivity - cost

        deviation_payoffs = {
            t: self.wages['no_edu'] for t in self.types
        }

        ic = all(payoffs[t] >= deviation_payoffs[t] for t in self.types)
        return ic, payoffs

if __name__ == "__main__":
    game = JobMarketSignalingGame()

    sep_eq, sep_decisions, sep_payoffs = game.separating_equilibrium()
    print("Separating Equilibrium:", sep_eq)
    print("  Decisions:", sep_decisions)
    print("  Payoffs:", sep_payoffs)

    pool_eq, pool_payoffs = game.pooling_equilibrium()
    print("Pooling Equilibrium (both get edu):", pool_eq)
    print("  Payoffs:", pool_payoffs)