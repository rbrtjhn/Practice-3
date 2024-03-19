def count_character_frequency(input_string):

    # Create a dictionary to store character frequencies
    frequency = {}

    # Iterate through each character in the input string
    for char in input_string:

        # Increment the frequency count for the current character
        frequency[char] = frequency.get(char, 0) + 1

    return frequency

#Testing the function
print("Name: Robert John Jotojot")
if __name__ == "__main__":
    input_string = input("Enter a string: ")

    # Calling the function to count character frequency
    char_frequency = count_character_frequency(input_string)

    # Printing the character frequency in a readable format
    print("Character frequency:")
    for char, freq in char_frequency.items():
        print(f"{char}: {freq}")