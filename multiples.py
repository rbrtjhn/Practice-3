def sum_of_multiples(num1, num2, limit):

    # Initialize the sum to 0
    total_sum = 0

    # Iterate through each number from 1 up to but not including the limit
    for i in range(1, limit):

        # If the number is a multiple of num1 or num2, add it to the sum
        if i % num1 == 0 or i % num2 == 0:
            total_sum += i
    return total_sum

# Testing the function
print("Name: Robert John Jotojot")
if __name__ == "__main__":
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    limit = int(input("Enter the limit: "))
    
    result = sum_of_multiples(first_number, second_number, limit)
    print(f"The sum of multiples of {first_number} or {second_number} up to {limit} is {result}.")