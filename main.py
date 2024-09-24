# Function to open a file and write to it
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}.")

# Function to read content from a file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"{filename} not found.")

# Function to append content to a file
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
    print(f"Content appended to {filename}.")

# Function to count the number of lines, words, and characters in a file
def file_statistics(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        lines = content.splitlines()
        words = content.split()
        characters = len(content)
        
        print(f"Statistics for {filename}:")
        print(f"Number of lines: {len(lines)}")
        print(f"Number of words: {len(words)}")
        print(f"Number of characters: {characters}")
    except FileNotFoundError:
        print(f"{filename} not found.")

# Main function to demonstrate file operations
def main():
    filename = 'example.txt'
    
    # Writing content to the file
    write_to_file(filename, "This is the first line.\nThis is the second line.\n")
    
    # Reading content from the file
    read_from_file(filename)
    
    # Appending content to the file
    append_to_file(filename, "This is an appended line.\n")
    
    # Reading content again to see the changes
    read_from_file(filename)
    
    # Displaying statistics of the file
    file_statistics(filename)

# Run the main function
if __name__ == "__main__":
    main()
