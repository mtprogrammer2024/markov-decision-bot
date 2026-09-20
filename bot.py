import random


class QLearningBot:
    """A small tabular Q-learning agent."""

    def __init__(
        self,
        environment,
        learning_rate=0.10,
        discount_factor=0.90,
        exploration_rate=0.10,
    ):
        self.environment = environment

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

        self.q_table = {}
        self.current_state = None

    def start(self, state):
        self.current_state = state

    def get_q_values(self, state):

        if state not in self.q_table:
            self.q_table[state] = {
                action: 0.0
                for action in self.environment.states
            }

        return self.q_table[state]

    def choose_action(self):

        q_values = self.get_q_values(self.current_state)

        actions = list(q_values.keys())

        # Exploration
        if random.random() < self.exploration_rate:
            return random.choice(actions)

        # Exploitation
        max_value = max(q_values.values())

        best_actions = [
            action
            for action, value in q_values.items()
            if value == max_value
        ]

        return random.choice(best_actions)

    def learn(self, state, action, reward, next_state):

        current_q = self.get_q_values(state)[action]

        next_q_values = self.get_q_values(next_state)

        max_next_q = max(next_q_values.values())

        # Q-Learning formula
        new_q = current_q + self.learning_rate * (
            reward
            + self.discount_factor * max_next_q
            - current_q
        )

        self.q_table[state][action] = new_q

    def step(self):

        state = self.current_state

        action = self.choose_action()

        next_state, reward = self.environment.step(action)

        self.learn(
            state,
            action,
            reward,
            next_state,
        )

        self.current_state = next_state

        return state, action, reward, next_state