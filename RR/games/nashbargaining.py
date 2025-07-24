import numpy as np
from scipy.optimize import minimize

class NashBargaining:
    def __init__(self, feasible_set, disagreement_point):
        """
        feasible_set: list of tuples (u1, u2) representing the feasible utility outcomes
        disagreement_point: tuple (d1, d2)
        """
        self.feasible = np.array(feasible_set)
        self.d = np.array(disagreement_point)

        # Only keep points that Pareto dominate the disagreement point
        self.pareto_set = self.feasible[np.all(self.feasible >= self.d, axis=1)]

    def solve(self):
        def nash_product(x):
            return -(x[0] - self.d[0]) * (x[1] - self.d[1])  # negative for minimization

        # Constraints: x in convex hull of feasible points, and dominates disagreement
        bounds = [(min(self.pareto_set[:, 0]), max(self.pareto_set[:, 0])),
                  (min(self.pareto_set[:, 1]), max(self.pareto_set[:, 1]))]

        constraints = {'type': 'ineq', 'fun': lambda x: x - self.d}

        # Start at midpoint of Pareto set
        x0 = np.mean(self.pareto_set, axis=0)
        result = minimize(nash_product, x0, bounds=bounds, constraints=constraints)

        if result.success:
            return result.x
        else:
            raise ValueError("Nash solution could not be found.")

# Example usage
if __name__ == "__main__":
    feasible_set = [(2, 1), (1, 2), (2, 2), (3, 1), (1, 3)]
    disagreement_point = (0, 0)
    game = NashBargaining(feasible_set, disagreement_point)
    solution = game.solve()
    print("Nash Bargaining Solution:", solution)