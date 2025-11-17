import random
print("Welcome to Rock-Paper-Scissors!")
rng = random.randint(1,3)
if rng == 1:
    choice = "rock"
elif rng == 2:
    choice = "paper"
elif rng == 3:
    choice = "scissors"
print(f"Computer chose: {choice}")