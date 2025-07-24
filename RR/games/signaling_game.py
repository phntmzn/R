import random

class SignalingGame:
    def __init__(self, prob_high=0.5):
        # Type probabilities
        self.prior = {'H': prob_high, 'L': 1 - prob_high}
        self.types = ['H', 'L']
        self.signals = ['s1', 's2']
        self.actions = ['a1', 'a2']
        
        # Payoff matrices: U_S[type][signal][receiver_action], U_R[type][signal][receiver_action]
        self.U_S = {
            'H': {'s1': {'a1': 2, 'a2': 1}, 's2': {'a1': 1, 'a2': 0}},
            'L': {'s1': {'a1': 1, 'a2': 0}, 's2': {'a1': 2, 'a2': 1}},
        }
        self.U_R = {
            'H': {'s1': {'a1': 2, 'a2': 0}, 's2': {'a1': 1, 'a2': -1}},
            'L': {'s1': {'a1': -1, 'a2': 1}, 's2': {'a1': 0, 'a2': 2}},
        }

    def sender_strategy(self, theta):
        # Example separating equilibrium: H → s1, L → s2
        return 's1' if theta == 'H' else 's2'

    def receiver_belief(self, signal):
        # Belief µ(type | signal)
        if signal == 's1':
            return {'H': 1.0, 'L': 0.0}
        else:
            return {'H': 0.0, 'L': 1.0}

    def receiver_best_response(self, signal):
        beliefs = self.receiver_belief(signal)
        expected_util = {}
        for action in self.actions:
            expected_util[action] = sum(
                beliefs[theta] * self.U_R[theta][signal][action]
                for theta in self.types
            )
        return max(expected_util, key=expected_util.get)

    def play(self):
        # Nature draws type
        theta = 'H' if random.random() < self.prior['H'] else 'L'
        signal = self.sender_strategy(theta)
        action = self.receiver_best_response(signal)

        sender_payoff = self.U_S[theta][signal][action]
        receiver_payoff = self.U_R[theta][signal][action]

        return {
            "theta": theta,
            "signal": signal,
            "action": action,
            "sender_payoff": sender_payoff,
            "receiver_payoff": receiver_payoff
        }

if __name__ == "__main__":
    game = SignalingGame()
    result = game.play()
    print(result)

