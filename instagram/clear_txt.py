def clear_file(filename):
    try:
        with open(filename, 'w') as file:
            file.truncate(0)
        print(f"Contents of {filename} have been cleared successfully.")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access {filename}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    filename = "reels.txt"
    clear_file(filename)