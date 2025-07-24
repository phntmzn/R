


class ProductiveEducationJobMarketGame:
    def __init__(self):
        self.types = ['high', 'low']
        self.prior = {'high': 0.5, 'low': 0.5}
        self.education_cost = {'high': 1, 'low': 3}
        self.base_productivity = {'high': 3, 'low': 1}
        self.edu_bonus = 2  # Education boosts productivity for both types

    def productivity(self, t, edu):
        """
        Returns productivity: base + bonus if educated
        """
        base = self.base_productivity[t]
        return base + self.edu_bonus if edu else base

    def wage_offer(self, observed_edu):
        """
        Firm observes education and computes expected productivity
        """
        exp_prod = 0.0
        total_prob = 0.0
        for t in self.types:
            prob = self.prior[t]
            prod = self.productivity(t, observed_edu)
            exp_prod += prob * prod
            total_prob += prob
        return exp_prod / total_prob

    def evaluate_strategy(self, decisions):
        """
        Input: decisions = {'high': True/False, 'low': True/False}
        Returns: payoffs to both types and wage offered
        """
        educated = any(decisions[t] for t in self.types)
        wage = self.wage_offer(educated)

        payoffs = {}
        for t in self.types:
            edu = decisions[t]
            cost = self.education_cost[t] if edu else 0
            payoffs[t] = wage - cost

        return wage, payoffs

if __name__ == "__main__":
    game = ProductiveEducationJobMarketGame()

    sep_decisions = {'high': True, 'low': False}
    pool_decisions = {'high': True, 'low': True}

    print("== Separating ==")
    sep_wage, sep_payoffs = game.evaluate_strategy(sep_decisions)
    print(f"Wage offered: {sep_wage:.2f}")
    print(f"Payoffs: {sep_payoffs}")

    print("\n== Pooling ==")
    pool_wage, pool_payoffs = game.evaluate_strategy(pool_decisions)
    print(f"Wage offered: {pool_wage:.2f}")
    print(f"Payoffs: {pool_payoffs}")