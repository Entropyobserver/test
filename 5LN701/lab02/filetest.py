"""
def get_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."
    except IOError:
        return "Error reading file."

def get_lines_readlines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return ''.join(lines)
    except FileNotFoundError:
        return "File not found."
    except IOError:
        return "Error reading file."

def test_file_reading_methods():
    # Create test file
    with open('test_file.txt', 'w') as file:
        file.write("This is a test file.\nIt has multiple lines.\n")
    
    # Test read() method
    assert get_lines('test_file.txt') == "This is a test file.\nIt has multiple lines.\n", "Test failed: read() method content does not match."
    
    # Test readlines() method
    assert get_lines_readlines('test_file.txt') == "This is a test file.\nIt has multiple lines.\n", "Test failed: readlines() method content does not match."
    
    # Test non-existent file
    assert get_lines('non_existent_file.txt') == "File not found.", "Test failed: File not found error not handled correctly."
    assert get_lines_readlines('non_existent_file.txt') == "File not found.", "Test failed: File not found error not handled correctly."
    
    print("All tests passed.")

# Run the test
test_file_reading_methods()
"""
def read_file_methods(file_path):
    # Method 1: read() - entire file as a single string
    print("--- Method 1: read() ---")
    with open(file_path, 'r') as file:
        content_read = file.read()
        print(f"Total characters: {len(content_read)}")
        print(f"First 200 characters:\n{content_read[:200]}")
    
    # Method 2: readlines() - list of lines
    print("\n--- Method 2: readlines() ---")
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Total lines: {len(lines)}")
        print(f"First 5 lines:\n{''.join(lines[:5])}")
    
    # Method 3: readline() - read line by line
    print("\n--- Method 3: readline() ---")
    with open(file_path, 'r') as file:
        first_line = file.readline()
        print(f"First line: {first_line}")
        print(f"First line length: {len(first_line)}")
    
    # Method 4: iterate through file
    print("\n--- Method 4: Iteration ---")
    with open(file_path, 'r') as file:
        line_count = 0
        word_count = 0
        for line in file:
            line_count += 1
            word_count += len(line.split())
            if line_count == 5:  # Show first 5 lines
                print(f"First 5 lines (iteration):\n{line}")
        print(f"Total lines found: {line_count}")
        print(f"Total words found: {word_count}")

# Replace with your actual file path
file_path = '/home/yaxi4987/5LN701/lab02/wiki.train_1147.raw'
read_file_methods(file_path)