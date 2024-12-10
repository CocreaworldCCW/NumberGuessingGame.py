import math

def logarithm_binary_search(range_min, range_max, target):
    attempts = 0
    log_min = math.log10(range_min)
    log_max = math.log10(range_max)
    while log_max - log_min > 0.5:  # Larger threshold for switching
        mid_log = (log_min + log_max) / 2
        mid_val = 10 ** mid_log
        attempts += 1
        print(f"Guess: ~{int(mid_val)} (log = {mid_log})")
        if mid_val == target:
            print(f"Found the number in {attempts} guesses!")
            return
        elif mid_val < target:
            log_min = mid_log
        else:
            log_max = mid_log
          range_min = int(10 ** log_min)
    range_max = int(10 ** log_max)
    print(f"Switching to binary search within {range_min} to {range_max}")
    binary_search(range_min, range_max, target) # This part, use with previous file
