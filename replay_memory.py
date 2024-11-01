import random
from collections import deque

class ReplayMemory:
    def __init__(self, capacity):
        self.memory = deque(maxlen=capacity)

    def add_experience(self, state, action, reward, next_state, done):
        experience = (state, action, reward, next_state, done)
        self.memory.append(experience)

    def sample_experiences(self, batch_size):
        return random.sample(self.memory, batch_size)

memory = ReplayMemory(capacity=1000)
memory.add_experience([1,0], "move", 1, [1,1], False)
print(memory.sample_experiences(1))

