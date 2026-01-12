import os
import shutil

def organize_folder(target_path):
    # Dictionary mapping folder names to their associated extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".avif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Video": [".mp4", ".mov", ".avi", ".mkv"],
        "Archives": [".zip", ".tar", ".rar", ".7z", ".iso"],
        "Scripts": [".py", ".js", ".html", ".css", ".cpp"],
        "Software": [".exe", ".msi", ".dmg", ".apk"],
        "Design": [".psd", ".ai", ".xd", ".sketch", ".af"]
    }

    # Change the current working directory to the target path
    os.chdir(target_path)

    for file in os.listdir():
        # Skip directories, we only want to move files
        if os.path.isdir(file):
            continue

        # Get the file extension
        name, extension = os.path.splitext(file)
        extension = extension.lower()

        # Check which category the extension belongs to
        for folder, extensions in file_types.items():
            if extension in extensions:
                # Create the folder if it doesn't exist
                if not os.path.exists(folder):
                    os.makedirs(folder)
                
                # Move the file
                shutil.move(file, os.path.join(folder, file))
                print(f"Moved: {file} -> {folder}/")
                break

if __name__ == "__main__":
    # Replace this with the path to the folder you want to organize
    path_to_clean = input("Enter the full path of the folder to organize: ")
    organize_folder(path_to_clean)