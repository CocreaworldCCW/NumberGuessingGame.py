import math

def refined_pure_logarithm_search(range_min, range_max, target):
    import math
    attempts = 0
    log_min = math.log10(range_min)
    log_max = math.log10(range_max)
    
    while log_max - log_min > 1e-9:  # Precision threshold for unique determination
        mid_log = (log_min + log_max) / 2
        mid_val = 10 ** mid_log
        attempts += 1
        print(f"Guessing logarithm: {mid_log:.6f} (value: ~{int(mid_val)})")
        
        if math.floor(mid_val) == target:
            print(f"Found the number in {attempts} guesses!")
            return
        elif mid_val < target:
            log_min = mid_log
        else:
            log_max = mid_log

    # Output the final range when the logarithm difference is small enough
    guessed_value = round(10 ** ((log_min + log_max) / 2))
    print(f"Final answer is {guessed_value}, found in {attempts} guesses!")
