import os

def print_directory_contents(directory):
    # Ensure the directory path ends with a slash for proper joining
    if not directory.endswith(os.sep):
        directory += os.sep
    
    # List all files and directories in the given directory
    contents = os.listdir(directory)
    
    # Print each item in the directory
    for item in contents:
        print(item)

# Example usage: print contents of the current directory
print_directory_contents('.')

print_directory_contents('C:')
