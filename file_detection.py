# File dection

import os

file_path = "readme.txt"

# Check if the file exists
if os.path.exists(file_path):
    print(f"File {file_path} exists")

    if os.path.isfile(file_path):
        print(f"It is a regular file")
    elif os.path.isdir(file_path):
        print(f"It is a directory")
    
else:
    print(f"File {file_path} does not exist")
    # Get the file size in bytes
    # file_size_bytes = os.path.getsize(file_path)
    
    # # Convert bytes to kilobytes
    # file_size_kilobytes = file_size_bytes / 1024
    
    # # Convert kilobytes to megabytes
    # file_size_megabytes = file_size_kilobytes / 1024
    
    # # Print the file size
    # print(f"File size: {file_size_megabytes:.2f} MB")
