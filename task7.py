import random
from collections import defaultdict

nums = 2_000_000

counts = defaultdict(int)

for _ in range(nums):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    counts[dice1 + dice2] += 1

probabilities = {key: value / nums for key, value in counts.items()}

keys = sorted(probabilities.keys())

print("| Dice | Probability |")
print("|------|-------------|")
for key in keys:
    print(f"| {key:4} | {probabilities[key]:11.2%} |")
