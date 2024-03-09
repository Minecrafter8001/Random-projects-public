import os
import time

true = True

def is_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Try to read a small portion of the file content
            # and check if it can be decoded as text
            sample_content = f.read(1024)  # Read the first 1024 bytes
            sample_content.encode('utf-8').decode('utf-8')  # Try to decode the content
            return True  # If decoding succeeds, it's likely a text file
    except UnicodeDecodeError:
        return False  # If decoding fails, it's not a text file
    except Exception as e:
        print(f"An error occurred: {e}")
        return False  # Handle other exceptions gracefully

def live_tail(file_path, interval=1):
    # Live tails a text file.
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not a valid file path.")
        return
    if not is_text_file(file_path):
        print(f"Error: {file_path} does not contain text.")
        return
    
    with open(file_path, 'r') as file:
        # Move cursor to the end of the file
        file.seek(0, 2)
        
        # Continuously read new lines
        while true:
            line = file.readline()
            if line:
                print(line, end='')  # Print the line without adding newline
            else:
                time.sleep(interval)  # Wait for new content

if __name__ == "__main__":
    while true:
        file_path = input("Input the path of the file to read: ")
        live_tail(file_path)
