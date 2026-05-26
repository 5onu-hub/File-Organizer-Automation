import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# =========================
# LOGGING SETUP
# =========================

logging.basicConfig(
    filename='logs/organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# =========================
# FOLDER PATH
# =========================

SOURCE_FOLDER = "monitored_folder"

DESTINATION_FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3"],
    "Documents": [".docx", ".txt", ".pptx"],
    "Python_Files": [".py"]
}

# =========================
# CREATE FOLDERS
# =========================

for folder_name in DESTINATION_FOLDERS.keys():
    os.makedirs(f"folders/{folder_name}", exist_ok=True)

os.makedirs("logs", exist_ok=True)

# =========================
# ORGANIZE FUNCTION
# =========================

def organize_file(file_path):
    if os.path.isdir(file_path):
        return

    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_name)[1].lower()

    for folder, extensions in DESTINATION_FOLDERS.items():
        if extension in extensions:

            destination_path = os.path.join(
                "folders",
                folder,
                file_name
            )

            try:
                shutil.move(file_path, destination_path)

                print(f"Moved: {file_name} → {folder}")

                logging.info(
                    f"Moved {file_name} to {folder}"
                )

            except Exception as e:
                print("Error:", e)

            break

# =========================
# WATCHDOG EVENT
# =========================

class FileHandler(FileSystemEventHandler):

    def on_created(self, event):
        time.sleep(1)
        organize_file(event.src_path)

# =========================
# START MONITORING
# =========================

event_handler = FileHandler()
observer = Observer()

observer.schedule(
    event_handler,
    SOURCE_FOLDER,
    recursive=False
)

observer.start()

print("📂 File Organizer Running...")

try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    observer.stop()

observer.join()