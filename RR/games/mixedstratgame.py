import numpy as np
import itertools
from scipy.optimize import linprog

class MixedStrategyGame:
    def __init__(self, payoffs_p1, payoffs_p2):
        """
        Assumes a 2-player bimatrix game.
        payoffs_p1, payoffs_p2: m x n matrices of payoffs for player 1 and 2
        """
        self.A = np.array(payoffs_p1)
        self.B = np.array(payoffs_p2)
        self.m, self.n = self.A.shape

    def best_response_lp(self, A):
        """
        Given an opponent's strategy, compute best response via LP.
        A is the payoff matrix for the responding player.
        """
        c = [-1.0] + [0.0] * A.shape[0]  # Maximize v
        A_ub = np.hstack((-np.ones((A.shape[1], 1)), A.T))  # Constraints: v <= a^T x
        b_ub = np.zeros(A.shape[1])
        A_eq = [[0.0] + [1.0] * A.shape[0]]  # sum x = 1
        b_eq = [1.0]
        bounds = [(None, None)] + [(0.0, 1.0)] * A.shape[0]

        result = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds, method="highs")
        return result.x[1:] if result.success else None

    def compute_mixed_equilibrium(self):
        """
        Use support enumeration for simplicity (small games only).
        Returns one Nash equilibrium as mixed strategies (p1_strategy, p2_strategy).
        """
        strategies_p1 = list(itertools.product([0, 1], repeat=self.m))
        strategies_p2 = list(itertools.product([0, 1], repeat=self.n))

        for s1 in strategies_p1:
            if sum(s1) == 0: continue
            support1 = [i for i, val in enumerate(s1) if val == 1]
            for s2 in strategies_p2:
                if sum(s2) == 0: continue
                support2 = [j for j, val in enumerate(s2) if val == 1]

                A_sub = self.A[np.ix_(support1, support2)]
                B_sub = self.B[np.ix_(support1, support2)]

                try:
                    # Player 1
                    p2 = np.ones(len(support2)) / len(support2)
                    expected_p1 = A_sub @ p2
                    if not np.allclose(expected_p1, expected_p1[0]):
                        continue
                    # Player 2
                    p1 = np.ones(len(support1)) / len(support1)
                    expected_p2 = B_sub.T @ p1
                    if not np.allclose(expected_p2, expected_p2[0]):
                        continue

                    # Embed back into full strategy vector
                    strat1 = np.zeros(self.m)
                    strat2 = np.zeros(self.n)
                    strat1[support1] = 1 / len(support1)
                    strat2[support2] = 1 / len(support2)
                    return strat1, strat2
                except:
                    continue

        return None, None
    
if __name__ == "__main__":
    A = [[2, 0],
         [0, 1]]  # Player 1
    B = [[1, 0],
         [0, 2]]  # Player 2

    game = MixedStrategyGame(A, B)
    eq1, eq2 = game.compute_mixed_equilibrium()
    print("Mixed Strategy Equilibrium:")
    print("Player 1:", eq1)
    print("Player 2:", eq2)