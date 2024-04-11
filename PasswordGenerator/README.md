# Random Password Generator

This Python script generates a random password consisting of alphabets (both lowercase and uppercase) and digits.

## Description of Each Line:

1. `import random`: Imports the `random` module for generating random numbers and choices.
2. `Lalpha = "abcdefghijklmnopqrstuvwxyz"`: Defines a string containing lowercase alphabets.
3. `Ualpha = Lalpha.upper()`: Converts the lowercase alphabet string to uppercase.
4. `length = 16`: Sets the length of the generated password.
5. `nums = []`, `lower = []`, `upper = []`: Initializes empty lists to store digits, lowercase alphabets, and uppercase alphabets, respectively.
6. `for num in range(0, 10):`, `for char in Lalpha:`, `for char in Ualpha:`: Loops to populate the lists `nums`, `lower`, and `upper` with digits, lowercase alphabets, and uppercase alphabets, respectively.
7. `Pass = ""`: Initializes an empty string to store the generated password.
8. `already = []`: Initializes an empty list to keep track of the types of characters already added to the password.
9. `c = 0`: Initializes a counter variable.
10. `while c < length:`: Starts a while loop to generate the password until it reaches the desired length.
11. `x = random.randint(1, 3)`: Generates a random number between 1 and 3 to determine the type of character to add to the password.
12. `if x not in already:`: Checks if the randomly generated number has not been used before.
13. `if x == 1:`, `elif x == 2:`, `elif x == 3:`: Checks the value of `x` and chooses a character from the corresponding list (`nums`, `lower`, `upper`) to add to the password.
14. `else:`: Executes if the generated number has been used before.
15. `already = []`: Clears the list of characters added to the password.
16. `c -= 1`: Decrements the counter to ensure the loop generates the correct password length.
17. `c += 1`: Increments the counter.
18. `print(Pass)`: Prints the generated password.

## Repository URL:
[Link to Repository](https://github.com/SirSevrus/Tutorials)
