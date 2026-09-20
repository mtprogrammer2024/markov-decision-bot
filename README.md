# Markov Decision Bot

A small offline Python project combining Markov Chains and Q-Learning.

The project demonstrates how an agent can learn better decisions from experience.

## Features

- Markov Chain
- Transition probabilities
- Environment simulation
- Rewards
- Q-Table
- Q-Learning
- Exploration vs Exploitation
- Learning Rate
- Discount Factor
- Reward trend
- No API
- No server
- No external Python packages

## Project Structure

markov-decision-bot/

├── bot.py
├── environment.py
├── markov.py
├── main.py
└── README.md

## How It Works

The system has an environment and an intelligent agent.

The agent chooses an action.

The environment returns:

- Next state
- Reward

The agent then updates its Q-Table.

This process repeats many times.

## States

The example contains:

- ATTACK
- DEFEND
- IDLE

## Rewards

| Action | Result | Reward |
|---|---|---:|
| ATTACK | Success | +10 |
| ATTACK | Failure | -5 |
| DEFEND | Success | +5 |
| DEFEND | Failure | -1 |
| IDLE | Always | -2 |

## Q-Learning

The main formula is:

Q(s,a) = Q(s,a) + alpha * (
    reward
    + gamma * max(Q(next_state))
    - Q(s,a)
)

Where:

- alpha = learning rate
- gamma = discount factor
- reward = immediate reward
- Q(s,a) = current action value

## Exploration vs Exploitation

The bot sometimes explores new actions.

Example:

exploration_rate = 0.10

This means the bot has a 10% chance of trying a random action.

The remaining time it uses what it currently believes is the best action.

## Running the Project

Open a terminal inside the project folder.

Run:

python main.py

## Requirements

Python 3.x

No external packages are required.

No pip install is required.

No API key is required.

No internet connection is required.

No database is required.

No server is required.

## Goal

This project is intentionally small.

It is designed to demonstrate the basic ideas behind:

- Markov Models
- Reinforcement Learning
- Q-Learning
- Decision Making

   👤 سازنده

**مهدی طلوعی**

- GitHub: [@mtprogrammer2024](https://github.com/mtprogrammer2024)
- Email: mt.programmer2024@gmail.com
- LinkedIn: https://www.linkedin.com/in/mahditoloee/
