import numpy as np
from scipy.optimize import linprog

class MatrixGame:
    def __init__(self, A):
        self.A = np.array(A, dtype=float)  # m x n payoff matrix
        self.m, self.n = self.A.shape

    def solve_player1(self):
        """
        Solve for player 1’s optimal mixed strategy using LP:
        Maximize v such that Ax ≥ v and sum(x) = 1
        """
        # Convert to standard LP form: minimize -v
        c = np.zeros(self.m + 1)
        c[-1] = -1  # maximize v ↔ minimize -v

        # Constraints: A.T @ x ≥ v ↔ A.T @ x - v ≥ 0
        A_ub = np.hstack([-self.A.T, np.ones((self.n, 1))])
        b_ub = np.zeros(self.n)

        # Constraint: sum(x) = 1
        A_eq = np.hstack([np.ones((1, self.m)), np.zeros((1, 1))])
        b_eq = [1]

        bounds = [(0, 1)] * self.m + [(None, None)]

        res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
        if res.success:
            strategy = res.x[:-1]
            value = res.x[-1]
            return strategy, value
        else:
            raise ValueError("Linear program failed to solve.")

    def solve_player2(self):
        """
        Solve for player 2’s optimal mixed strategy by solving dual LP.
        """
        # Player 2 minimizes expected payoff
        c = np.zeros(self.n + 1)
        c[-1] = 1  # minimize v

        # Constraints: A @ y ≤ v ↔ A @ y - v ≤ 0
        A_ub = np.hstack([self.A, -np.ones((self.m, 1))])
        b_ub = np.zeros(self.m)

        # Constraint: sum(y) = 1
        A_eq = np.hstack([np.ones((1, self.n)), np.zeros((1, 1))])
        b_eq = [1]

        bounds = [(0, 1)] * self.n + [(None, None)]

        res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
        if res.success:
            strategy = res.x[:-1]
            value = res.x[-1]
            return strategy, value
        else:
            raise ValueError("Linear program failed to solve.")

    def solve(self):
        """
        Solve the game for both players.
        """
        p1_strategy, p1_value = self.solve_player1()
        p2_strategy, p2_value = self.solve_player2()

        assert np.isclose(p1_value, p2_value), "Game value mismatch!"
        return {
            'value': p1_value,
            'player1_strategy': p1_strategy,
            'player2_strategy': p2_strategy
        }

# Example usage
if __name__ == "__main__":
    A = [
        [1, -1],
        [-1, 1]
    ]
    game = MatrixGame(A)
    result = game.solve()
    print("Game value:", result['value'])
    print("Player 1 strategy:", result['player1_strategy'])
    print("Player 2 strategy:", result['player2_strategy'])

