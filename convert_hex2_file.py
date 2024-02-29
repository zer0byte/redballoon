import subprocess

# Open the file "hexe2" for reading and "7zipped" for writing in binary mode
with open("hex2", "r") as input_file, open("7zipped", "wb") as output_file:
    # Read each line in the input file
    for line in input_file:
        # Split the line by spaces to get the hex characters
        hex_chars = line.strip().split()
        for chars in hex_chars:
            # Extract all hex pairs using a regular expression
            all_hex = chars
            # Convert each hex pair to binary and write to the output file
            for c in [all_hex[i:i+2] for i in range(0, len(all_hex), 2)]:
                output_file.write(bytes.fromhex(c))

# Use subprocess to call 7z and extract the "7zipped" file
subprocess.run(["7z", "x", "7zipped"])

# Display the contents of the "dontfuckitup" file
with open("dontfuckitup", "r") as file:
    print(file.read())
