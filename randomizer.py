import random

def generate_random(min_val, max_val):
    return random.randint(min_val, max_val)

if __name__ == "__main__":
    print("🎲 Random Number Generator (Python)")
    min_val = int(input("Enter minimum: "))
    max_val = int(input("Enter maximum: "))
    print(f"Your random number: {generate_random(min_val, max_val)}")
