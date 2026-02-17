import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.getcwd()

FILE_DICT = {
    'PDFs': '.pdf',
    'Images': ['.jpg','.jpeg','.png'],
    'Text_files': '.txt'
}

def get_dest_folder(ext):
    for f, e in FILE_DICT.items():
            if ext in e:
                return f
    return 'Others'

class MyEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        #print(f"\nfile_path - {file_path}\n")
        ext = os.path.splitext(file_path)[1].lower()
        dest_folder = get_dest_folder(ext)
        os.makedirs(dest_folder, exist_ok= True)
        full_path = os.path.join(dest_folder, os.path.basename(file_path))
        try:
            shutil.move(file_path, full_path)
            print(f"Moved: {file_path} -> {full_path}")
        except:
             print("Failed to move the file")

if __name__ == "__main__":
    print(f"\nWatching the folder {WATCH_FOLDER} ...\n")
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
          while True:
               pass
    except KeyboardInterrupt:
          print("Stoped watching the folder.")
          observer.stop()
    observer.join()

    