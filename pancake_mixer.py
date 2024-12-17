import random
import re

# Function to validate the stack
def is_valid_stack(stack):
    size = len(stack)
    for i in range(size):
        pancake = stack[i]

        if pancake == 'O':
            if i == 0 or i == size - 1:
                return False  # Orange cannot be on the edge
            if stack[i-1] == '' or stack[i+1] == '':
                return False  # Orange must connect to two other pancakes

        elif pancake == 'Y':
            if (i == 0 or stack[i-1] != 'Y') and (i == size - 1 or stack[i+1] != 'Y'):
                return False  # Yellow must be adjacent to another Yellow

        elif pancake == 'W':
            if i > 0 and i < size - 1:
                if stack[i-1] != stack[i+1]:
                    return False  # White must have identical pancakes on both sides

        elif pancake == 'G':
            if i > 0 and i < size - 1:
                if stack[i-1] == stack[i+1]:
                    return False  # Grey must have different adjacent pancakes

    return True

# Function to generate a valid stack
def generate_stack(size, pancake_string, max_attempts=1000):
    pancake_types = ['O', 'Y', 'W', 'G']
    initial_pancakes = list(pancake_string.upper())
    tried_stacks = set()

    for attempt in range(max_attempts):
        stack = [''] * size

        # Ensure the required pancakes are included in the stack
        current_pancakes = initial_pancakes.copy()

        # Fill in the rest of the stack with random pancakes
        while len(current_pancakes) < size:
            current_pancakes.append(random.choice(pancake_types))

        # Shuffle the stack to randomize positions
        random.shuffle(current_pancakes)

        # Assign shuffled pancakes to the stack
        for i in range(size):
            stack[i] = current_pancakes[i]

        stack_tuple = tuple(stack)
        if stack_tuple in tried_stacks:
            continue
        tried_stacks.add(stack_tuple)

        # Validate the stack
        if is_valid_stack(stack):
            return ''.join(stack), attempt + 1  # Return stack and attempt number

    return "Error: Maximum attempts reached. Unable to find a valid stack.", max_attempts

# Function to parse the input
def parse_input(input_str):
    match = re.match(r"(\d+)([A-Za-z]+)", input_str)
    if match:
        size = int(match.group(1))
        pancake_string = match.group(2).upper()
        return size, pancake_string
    else:
        print("Invalid input format. Please provide a valid size and pancake string.")
        print("Format Guide: Enter the stack size followed by the required pancakes.")
        print("Example: 4OG (4 is the size, O and G are the required pancakes)")
        return None, None

# Main function
def main():
    try:
        while True:
            user_input = input("Enter the pancake stack size and required pancakes (e.g., 4OG): ")
            size, pancake_string = parse_input(user_input)
            if size and pancake_string:
                final_stack, attempt = generate_stack(size, pancake_string)
                print(f"Generated stack: {final_stack}")
                print(f"Attempt number: {attempt}")
            else:
                print("Please try again with the correct format.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")

if __name__ == "__main__":
    main()