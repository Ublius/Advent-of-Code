number = []
with open("file.txt", "r") as file:
    for line in file:
        for word in line.split():
            # Extract the first and last digits from each word
            first_digit = next((char for char in word if char.isdigit()), None)
            last_digit = next((char for char in reversed(word) if char.isdigit()), None)

            # Combine the first and last digits and add to the list
            if first_digit is not None and last_digit is not None:
                num = int(first_digit + last_digit)
                number.append(num)

print(sum(number))