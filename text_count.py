with open("/usercode/files/books.txt") as f:
   #your code goes here
      # Read the lines from the file
    lines = f.readlines()

# Process each line to count the number of words by counting spaces
for i, line in enumerate(lines):
    # Strip any leading/trailing whitespace
    stripped_line = line.strip()
    # Count the number of spaces and add one to get the word count
    if stripped_line:
        word_count = stripped_line.count(' ') + 1
    else:
        word_count = 0
    # Print the result in the specified format
    print(f"Line {i+1}: {word_count} words")
