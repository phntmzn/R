# /Users/brx86/RR/game/grim_trigger.py

class GrimTrigger:
    def __init__(self):
        self.defected = False  # If opponent has ever defected, this becomes True

    def play(self, opponent_history):
        """
        Decide the next move based on opponent's past moves.

        Parameters:
        opponent_history (list of str): list of 'C' (cooperate) or 'D' (defect)

        Returns:
        str: 'C' for cooperate, 'D' for defect
        """
        if 'D' in opponent_history:
            self.defected = True
        return 'D' if self.defected else 'C'


# Example usage
if __name__ == "__main__":
    gt = GrimTrigger()
    opponent_moves = ['C', 'C', 'C', 'D', 'C', 'C']
    for i in range(len(opponent_moves)):
        move = gt.play(opponent_moves[:i])
        print(f"Round {i+1}: Opponent = {opponent_moves[i]}, GrimTrigger = {move}")