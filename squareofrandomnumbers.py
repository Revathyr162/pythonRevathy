import random

# Function to generate a list of random numbers
def generate_random_numbers(length):
    return [random.randint(1, 100) for _ in range(length)]

# Main function to square the numbers using map and lambda
def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))

# Function to print the result
def print_result(numbers, squared_numbers):
    print("Original Numbers:", numbers)
    print("Squared Numbers:", squared_numbers)

# Main function
def main():
    length = int(input("Enter the length of the list: "))
    numbers = generate_random_numbers(length)
    squared_numbers = square_numbers(numbers)
    print_result(numbers, squared_numbers)

if __name__ == "__main__":
    main()
