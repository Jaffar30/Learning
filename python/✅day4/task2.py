import random
# print heads or tails

# Heads : 1
# Tails : 0

# Way1
print(f"{'Heads'*random.randint(0,1) or 'Tails'}")
# Way2
print(random.choice(["Heads","Tails"]))