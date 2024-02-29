# Open the file "hexe1" for reading
with open("hex1", "r") as file:
    # Read each line in the file
    for line in file:
        # Split the line by spaces to get the hex characters
        hex_chars = line.strip().split()
        for chars in hex_chars:
            # Split the hex characters into pairs and reverse them
            # Python's slice notation makes it easy to reverse the string
            c1, c2 = chars[0:2], chars[2:4]
            # Convert the hex pairs to their ASCII representation and print
            # Use bytes.fromhex() to convert hex to binary and then decode
            print(bytes.fromhex(c2 + c1).decode('latin-1'), end='')
