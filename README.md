#  File Organizer Automation Tool — Complete Remade Version 🚀

A professional Python automation project that automatically monitors a folder and organizes files into categorized folders in real-time.

This project uses:

* Python
* Watchdog
* Logging
* File handling
* Automation concepts

Perfect for:
 Resume Projects
 Python Practice
 Internship Portfolio
 GitHub Showcase

---

#  Final Project Structure

```bash
File-Organizer-Automation/
│
├── organizer.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── logs/
│   └── organizer.log
│
├── monitored_folder/
│
└── folders/
    ├── Images/
    ├── PDFs/
    ├── Videos/
    ├── Music/
    ├── Documents/
    ├── Python_Files/
    ├── Archives/
    └── Others/
```

---

#  requirements.txt

```txt
watchdog
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

#  .gitignore

```gitignore
__pycache__/
*.pyc
logs/organizer.log
```

---

#  Main Python Code — organizer.py

```python
import os
import shutil
import logging
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ==========================================
# LOGGING SETUP
# ==========================================

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ==========================================
# SOURCE FOLDER
# ==========================================

SOURCE_FOLDER = "monitored_folder"

# Create source folder if not exists
os.makedirs(SOURCE_FOLDER, exist_ok=True)

# ==========================================
# FILE TYPE MAPPINGS
# ==========================================

FILE_TYPES = {

    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp"
    ],

    "PDFs": [
        ".pdf"
    ],

    "Videos": [
        ".mp4",
        ".mkv",
        ".avi"
    ],

    "Music": [
        ".mp3",
        ".wav"
    ],

    "Documents": [
        ".docx",
        ".txt",
        ".pptx",
        ".xlsx"
    ],

    "Python_Files": [
        ".py"
    ],

    "Archives": [
        ".zip",
        ".rar"
    ]
}

# ==========================================
# CREATE DESTINATION FOLDERS
# ==========================================

BASE_FOLDER = "folders"

os.makedirs(BASE_FOLDER, exist_ok=True)

for folder_name in FILE_TYPES.keys():
    os.makedirs(
        os.path.join(BASE_FOLDER, folder_name),
        exist_ok=True
    )

# Others folder
os.makedirs(
    os.path.join(BASE_FOLDER, "Others"),
    exist_ok=True
)

# ==========================================
# GENERATE UNIQUE FILE NAME
# ==========================================

def get_unique_filename(destination_path):

    if not os.path.exists(destination_path):
        return destination_path

    filename, extension = os.path.splitext(destination_path)

    counter = 1

    while True:

        new_name = f"{filename}({counter}){extension}"

        if not os.path.exists(new_name):
            return new_name

        counter += 1

# ==========================================
# ORGANIZE FILE FUNCTION
# ==========================================

def organize_file(file_path):

    # Ignore folders
    if os.path.isdir(file_path):
        return

    # Ignore temporary files
    if file_path.endswith(".tmp"):
        return

    file_name = os.path.basename(file_path)

    extension = os.path.splitext(file_name)[1].lower()

    moved = False

    # Find matching folder
    for folder_name, extensions in FILE_TYPES.items():

        if extension in extensions:

            destination_folder = os.path.join(
                BASE_FOLDER,
                folder_name
            )

            destination_path = os.path.join(
                destination_folder,
                file_name
            )

            # Prevent duplicate overwrite
            destination_path = get_unique_filename(
                destination_path
            )

            try:

                shutil.move(file_path, destination_path)

                print(f" Moved: {file_name} → {folder_name}")

                logging.info(
                    f"Moved {file_name} to {folder_name}"
                )

            except Exception as error:

                print(f" Error moving {file_name}")

                logging.error(str(error))

            moved = True
            break

    # Move unmatched files to Others
    if not moved:

        destination_folder = os.path.join(
            BASE_FOLDER,
            "Others"
        )

        destination_path = os.path.join(
            destination_folder,
            file_name
        )

        destination_path = get_unique_filename(
            destination_path
        )

        try:

            shutil.move(file_path, destination_path)

            print(f" Moved: {file_name} → Others")

            logging.info(
                f"Moved {file_name} to Others"
            )

        except Exception as error:

            print(f" Error moving {file_name}")

            logging.error(str(error))

# ==========================================
# WATCHDOG EVENT HANDLER
# ==========================================

class FileHandler(FileSystemEventHandler):

    def on_created(self, event):

        # Wait for file to fully copy
        time.sleep(1)

        organize_file(event.src_path)

# ==========================================
# START MONITORING
# ==========================================

event_handler = FileHandler()

observer = Observer()

observer.schedule(
    event_handler,
    SOURCE_FOLDER,
    recursive=False
)

observer.start()

print(" File Organizer Automation Running...")
print(f" Monitoring Folder: {SOURCE_FOLDER}")

try:

    while True:
        time.sleep(5)

except KeyboardInterrupt:

    observer.stop()

observer.join()
```

---

# ▶ How To Run

## Step 1 — Open terminal

```bash
cd File-Organizer-Automation
```

---

## Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3 — Run project

```bash
python organizer.py
```

---

#  Testing

Put files inside:

```bash
monitored_folder/
```

Example:

```bash
photo.jpg
resume.pdf
song.mp3
notes.txt
```

Automatically moves to:

```bash
folders/
```

---

#  Example Output

```bash
 File Organizer Automation Running...

 Moved: photo.jpg → Images
 Moved: resume.pdf → PDFs
 Moved: song.mp3 → Music
 Moved: random.xyz → Others
```

---

#  Log File Example

```bash
2026-05-27 01:20:10 - Moved photo.jpg to Images
2026-05-27 01:20:15 - Moved song.mp3 to Music
```

---

#   Features Included

*  Real-time monitoring
*  Auto folder creation
*  Duplicate file handling
*  Logging system
*  Unknown file handling
*  Error handling
*  Clean project structure

---

#  Resume Description

### Short Version

> Built a Python automation tool that organizes files into categorized folders using real-time monitoring and logging.

### Professional Version

> Developed an advanced Python-based file organization automation system using Watchdog and OS modules. Implemented real-time folder monitoring, duplicate file handling, automatic categorization, and logging for efficient file management.

---

#  Future Improvements

You can add:

* GUI using Tkinter
* Dark mode
* Drag & Drop support
* File size filters
* AI-based file categorization
* Auto-clean Downloads folder
* Convert to `.exe`

---

#  Skills Demonstrated

* Python Automation
* File Handling
* OOP Concepts
* Logging
* Real-time Systems
* OS Operations
* Error Handling
* Problem Solving


