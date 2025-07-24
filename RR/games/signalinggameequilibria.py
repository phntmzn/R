

class SignalingGameEquilibria:
    def __init__(self):
        self.types = ['H', 'L']
        self.signals = ['s1', 's2']
        self.actions = ['a1', 'a2']
        self.U_S = {
            'H': {'s1': {'a1': 2, 'a2': 0}, 's2': {'a1': 1, 'a2': 1}},
            'L': {'s1': {'a1': 0, 'a2': 2}, 's2': {'a1': 1, 'a2': 1}},
        }
        self.U_R = {
            'H': {'s1': {'a1': 2, 'a2': -1}, 's2': {'a1': 1, 'a2': 0}},
            'L': {'s1': {'a1': -1, 'a2': 2}, 's2': {'a1': 0, 'a2': 1}},
        }
        self.prior = {'H': 0.5, 'L': 0.5}

    def receiver_best_response(self, signal, belief):
        best_a, best_utility = None, float('-inf')
        for a in self.actions:
            expected_u = sum(belief[t] * self.U_R[t][signal][a] for t in self.types)
            if expected_u > best_utility:
                best_utility, best_a = expected_u, a
        return best_a

    def check_separating_equilibrium(self):
        # Assumption: H sends s1, L sends s2
        beliefs = {'s1': {'H': 1.0, 'L': 0.0}, 's2': {'H': 0.0, 'L': 1.0}}
        responses = {
            's1': self.receiver_best_response('s1', beliefs['s1']),
            's2': self.receiver_best_response('s2', beliefs['s2'])
        }
        for t in self.types:
            true_signal = 's1' if t == 'H' else 's2'
            alt_signal = 's2' if t == 'H' else 's1'
            true_u = self.U_S[t][true_signal][responses[true_signal]]
            dev_u = self.U_S[t][alt_signal][responses[alt_signal]]
            if dev_u > true_u:
                return False, f"{t} prefers to deviate"
        return True, responses

    def check_pooling_equilibrium(self, pool_signal='s1'):
        # Both types send the same signal
        belief = {
            'H': self.prior['H'] / (self.prior['H'] + self.prior['L']),
            'L': self.prior['L'] / (self.prior['H'] + self.prior['L'])
        }
        response = self.receiver_best_response(pool_signal, belief)
        for t in self.types:
            true_u = self.U_S[t][pool_signal][response]
            alt_signal = 's2' if pool_signal == 's1' else 's1'
            dev_u = self.U_S[t][alt_signal][response]
            if dev_u > true_u:
                return False, f"{t} prefers to deviate to {alt_signal}"
        return True, response

if __name__ == "__main__":
    game = SignalingGameEquilibria()
    sep_result, sep_info = game.check_separating_equilibrium()
    pool_result, pool_info = game.check_pooling_equilibrium()

    print("Separating Equilibrium:", sep_result, sep_info)
    print("Pooling Equilibrium (s1):", pool_result, pool_info)