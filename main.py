# Open the original text file and read all lines
with open("original_file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Remove whitespace and reverse each line
reversed_lines = [line.strip()[::-1] for line in lines]

# Print the result
print(reversed_lines)

# Save the reversed lines to a new file (overwrite if exists)
with open("reversed_file.txt", "w", encoding="utf-8") as output_file:
    for line in reversed_lines:
        output_file.write(line + "\n")
