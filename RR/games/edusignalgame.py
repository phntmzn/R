
class UtilityEducationSignalingGame:
    def __init__(self):
        self.types = ['high', 'low']
        self.prior = {'high': 0.5, 'low': 0.5}
        self.productivity = {'high': 3, 'low': 1}
        self.education_effect = {'high': 1.0, 'low': -2.0}  # Utility/disutility from education

    def expected_wage(self, education_level):
        """
        Compute expected productivity given observed education level
        """
        exp_prod = 0.0
        total_prob = 0.0
        for t in self.types:
            # Assume beliefs are based on education decisions
            prob = self.prior[t]
            prod = self.productivity[t]
            exp_prod += prob * prod
            total_prob += prob
        return exp_prod / total_prob

    def evaluate_strategy(self, strategy):
        """
        strategy: dict like {'high': True/False, 'low': True/False}
        returns: wages and utilities for each type
        """
        educated = any(strategy[t] for t in self.types)
        wage = self.expected_wage(educated)

        results = {}
        for t in self.types:
            edu = strategy[t]
            utility = wage
            if edu:
                utility += self.education_effect[t]
            results[t] = utility
        return wage, results

if __name__ == "__main__":
    game = UtilityEducationSignalingGame()

    sep_strategy = {'high': True, 'low': False}
    pool_strategy = {'high': True, 'low': True}

    print("== Separating Equilibrium ==")
    sep_wage, sep_util = game.evaluate_strategy(sep_strategy)
    print(f"Wage offered: {sep_wage:.2f}")
    print(f"Utilities: {sep_util}")

    print("\n== Pooling Equilibrium ==")
    pool_wage, pool_util = game.evaluate_strategy(pool_strategy)
    print(f"Wage offered: {pool_wage:.2f}")
    print(f"Utilities: {pool_util}")