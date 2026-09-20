from markov import MarkovChain
from environment import Environment
from bot import QLearningBot


EPISODES = 1000
STEPS_PER_EPISODE = 10


def print_markov_probabilities():

    print("=== Markov Chain ===")

    sequence = [
        "ATTACK",
        "DEFEND",
        "ATTACK",
        "ATTACK",
        "IDLE",
        "ATTACK",
        "DEFEND",
        "DEFEND",
        "ATTACK",
    ]

    markov = MarkovChain()

    markov.learn(sequence)

    for state in ["ATTACK", "DEFEND", "IDLE"]:

        probabilities = markov.probabilities(state)

        if not probabilities:
            continue

        print(f"\n{state}:")

        for next_state, probability in probabilities.items():
            print(
                f"  -> {next_state}: "
                f"{probability * 100:.1f}%"
            )


def print_q_table(bot):

    print("\n=== Q-Table ===")

    for state, actions in bot.q_table.items():

        print(f"\nState: {state}")

        for action, value in actions.items():

            print(
                f"  {action:<7} "
                f"{value:>8.2f}"
            )


def print_reward_chart(rewards, width=50, rows=10):

    if not rewards:
        return

    bucket_size = max(
        1,
        len(rewards) // width
    )

    buckets = [
        rewards[i:i + bucket_size]
        for i in range(
            0,
            len(rewards),
            bucket_size
        )
    ]

    values = [
        sum(bucket) / len(bucket)
        for bucket in buckets
    ]

    min_value = min(values)
    max_value = max(values)

    if max_value == min_value:

        levels = [
            rows // 2
            for _ in values
        ]

    else:

        levels = [
            round(
                (value - min_value)
                / (max_value - min_value)
                * (rows - 1)
            )
            for value in values
        ]

    print("\n=== Reward Trend ===")

    for row in reversed(range(rows)):

        line = "".join(
            "█" if level == row else " "
            for level in levels
        )

        print(line)

    print(
        f"min={min_value:.2f} "
        f"max={max_value:.2f}"
    )


def main():

    # -------------------------
    # Markov Chain
    # -------------------------

    print_markov_probabilities()

    # -------------------------
    # Environment
    # -------------------------

    environment = Environment()

    # -------------------------
    # Q-Learning Bot
    # -------------------------

    bot = QLearningBot(
        environment,
        learning_rate=0.10,
        discount_factor=0.90,
        exploration_rate=0.10,
    )

    bot.start("ATTACK")

    episode_rewards = []

    total_reward = 0

    print("\n=== Q-Learning ===")

    print(
        f"Episodes: {EPISODES}"
    )

    print(
        f"Steps per episode: "
        f"{STEPS_PER_EPISODE}\n"
    )

    # -------------------------
    # Training
    # -------------------------

    for episode in range(EPISODES):

        bot.start("ATTACK")

        episode_reward = 0

        for step in range(STEPS_PER_EPISODE):

            state, action, reward, next_state = bot.step()

            episode_reward += reward

            total_reward += reward

            # Show first episode
            if episode == 0 and step < 10:

                print(
                    f"{step + 1:02}. "
                    f"{state} -> {action} "
                    f"-> {next_state} "
                    f"| Reward: {reward:+}"
                )

        episode_rewards.append(
            episode_reward
        )

    # -------------------------
    # Results
    # -------------------------

    print_q_table(bot)

    print_reward_chart(
        episode_rewards
    )

    print("\n=== Summary ===")

    print(
        f"Total reward: "
        f"{total_reward}"
    )

    print(
        f"Average reward/episode: "
        f"{sum(episode_rewards) / len(episode_rewards):.2f}"
    )


if __name__ == "__main__":
    main()