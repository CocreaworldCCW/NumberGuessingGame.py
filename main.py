def main():
    print("Choose a method:")
    print("1. Pure Guess")
    print("2. Pure Binary Search")
    print("3. Logarithm + Binary Search")
    print("4. Pure Logarithm Search")
    method = int(input("Enter method number: "))
    range_min = int(input("Enter the lower bound of the range: "))
    range_max = int(input("Enter the upper bound of the range: "))
    target = int(input("Enter the target number (keep it hidden if playing with others): "))
    
    if method == 1:
        pure_guess(range_min, range_max, target)
    elif method == 2:
        binary_search(range_min, range_max, target)
    elif method == 3:
        logarithm_binary_search(range_min, range_max, target)
    elif method == 4:
        pure_logarithm_search(range_min, range_max, target)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
