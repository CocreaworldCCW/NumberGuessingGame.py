def pure_guess(range_min, range_max, target):
    import random
    attempts = 0
    while True:
        guess = random.randint(range_min, range_max)
        attempts += 1
        print(f"Guess: {guess}")
        if guess == target:
            print(f"Found the number in {attempts} guesses!")
            break
