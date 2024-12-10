def binary_search(range_min, range_max, target):
    attempts = 0
    while range_min <= range_max:
        guess = (range_min + range_max) // 2
        attempts += 1
        print(f"Guess: {guess}")
        if guess == target:
            print(f"Found the number in {attempts} guesses!")
            break
        elif guess < target:
            range_min = guess + 1
        else:
            range_max = guess - 1
