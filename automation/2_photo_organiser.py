import os

def rename_images(base_name, foldername):
    num = 1
    for file in os.listdir(foldername):
        if os.path.splitext(file)[1] in ['.jpg','.jpeg','.png']:
            os.rename(file, base_name+f'_{num}{os.path.splitext(file)[1]}')
            num+=1

def preview_changes(basename, foldername):
    num = 1
    print("Preview changes:")
    for file in os.listdir(foldername):
        if os.path.splitext(file)[1] in ['.jpg','.jpeg','.png']:
            print(f" - {file} -> {basename+f'_{num}{os.path.splitext(file)[1]}'}")
            num+=1
    
if __name__ == "__main__":
    while True:
        basename = input("Enter the base name for the imager: ").strip()
        if not basename:
            print("You must enter a name")
        else: break

    foldername = input("Enter the folder name or leave blank: ").strip() or os.getcwd()

    while True:
        choise = input("Enter 1 to preview, 2 to change and 3 to exit: ")
        match choise:
            case '1': preview_changes(basename,foldername)
            case '2': 
                rename_images(basename, foldername)
                print("✅ Image reorganisation is completed")
            case '3': break
            case _ : print("Enter a valid option")