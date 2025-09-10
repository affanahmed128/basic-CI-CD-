def write_to_file(filename, content):
    """Writes the given content to a file with the specified filename."""
    with open(filename, 'w') as file:
        file.write(content)
        
if __name__ == "__main__":
    write_to_file('output.txt', 'Hello from python script!')
    print("File is created and Content written to output.txt")
    