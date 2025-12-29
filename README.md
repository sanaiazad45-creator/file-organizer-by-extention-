## Python File Organizer by Extension

This Python script automatically organizes files into folders based on their file extensions.

## How It Works

- Scans a target folder
- Detects each fils's extension
- Creates folders for each extension 
- Moves files into corresponding folders

## Example

Before:

test_folder/
|---- image.jpg
|---- document.txt
|---- archive.zip

After:

|----- jpg/
      |____ image.jpg
|
|----- txt/
       |_____ document.txt
|
|----- zip/ 
      |_____ archive.zip

## How to Run

''' bash
python file_sorter.py

Make sure to update folder_path in the script to match your target folder.

Skills Demonstrated

. Python file handling ('os', 'shutil')
. Automation logic
. Use of os, shutil, and path modules
. Folder creation and file movement
. Error handling and path validation

Author

Azad Sanai
Python Developer | Automation & Data Workflow specialist
Loction: Denmark
