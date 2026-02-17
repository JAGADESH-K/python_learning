import os
import shutil

EXTENSION_MAP = {
    'PDFs': '.pdf',
    'Images': ['.jpg','.jpeg','.png'],
    'Text_files': '.txt'
}

def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for f, e in EXTENSION_MAP.items():
        if ext in e:
            return f
    return 'Others'

def sort_files(foldername):
    for file in os.listdir(foldername):
        if (not os.path.isdir(file)) and os.path.splitext(file)[1] != '.py':
            full_path = os.path.join(foldername, file)

            dest_folder = get_destination_folder(file)
            dest_file = os.path.join(dest_folder, file)

            os.makedirs(dest_folder, exist_ok=True)

            shutil.move(full_path, dest_file)
            
            print(f"Moved: {full_path} -> {dest_file}")
    

if __name__ == '__main__':
    folder = input("Enter the folder name or leave blank: ").strip()
    folder = folder or os.getcwd()

    if not os.path.exists(folder):
        print("Folder does not exist")
    else:
        sort_files(folder)
        print("✅ File Sorting completed")



    

