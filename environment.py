import random


class Environment:
    """Small simulated environment used by the Q-learning agent."""

    def __init__(self):
        self.states = ["ATTACK", "DEFEND", "IDLE"]

    def step(self, action):

        if action == "ATTACK":
            return self.attack()

        if action == "DEFEND":
            return self.defend()

        if action == "IDLE":
            return self.idle()

        return "IDLE", -5

    def attack(self):

        # 70% success
        if random.random() < 0.70:
            return "ATTACK", 10

        return "DEFEND", -5

    def defend(self):

        # 90% success
        if random.random() < 0.90:
            return "DEFEND", 5

        return "ATTACK", -1

    def idle(self):
        return "IDLE", -2