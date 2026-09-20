from collections import defaultdict


class MarkovChain:
    """Learn transition frequencies and probabilities from state sequences."""

    def __init__(self):
        self.transitions = defaultdict(lambda: defaultdict(int))

    def learn(self, sequence):
        for current, next_state in zip(sequence, sequence[1:]):
            self.learn_transition(current, next_state)

    def learn_transition(self, current, next_state):
        self.transitions[current][next_state] += 1

    def probabilities(self, current):
        transitions = self.transitions[current]
        total = sum(transitions.values())

        if total == 0:
            return {}

        return {
            state: count / total
            for state, count in transitions.items()
        }