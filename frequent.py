input_string=input("Enter the string:").lower()

# Initialize a list to store the frequency of each letter
char_count = [0] * 26  # Assuming only lowercase letters
# Count the frequency of each letter
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        index = ord(char) - ord('a')  # Convert the letter to an index (0-25)
        char_count[index]+= 1
# Create a list of tuples containing (letter, frequency) pairs
letter_freq = [(chr(i + ord('a')), freq) for i, freq in enumerate(char_count) if freq > 0]
# Sort the list based on frequency and then alphabetically
letter_freq.sort(key=lambda x: (-x[1], x[0]))
result = ''.join(letter for letter, _ in letter_freq)
print(result)