import os
import shutil

def organize_folder(target_path):
    # Dictionary mapping folder names to their associated extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".avif", ".webp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Video": [".mp4", ".mov", ".avi", ".mkv"],
        "Archives": [".zip", ".tar", ".rar", ".7z", ".iso"],
        "Scripts": [".py", ".js", ".html", ".css", ".cpp"],
        "Software": [".exe", ".msi", ".dmg", ".apk"],
        "Design": [".psd", ".ai", ".xd", ".sketch", ".af"]
    }

    try:
        os.chdir(target_path)
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
        return

    for file in os.listdir():
        if os.path.isdir(file):
            continue

        name, extension = os.path.splitext(file)
        extension = extension.lower()

        # Determine destination folder
        dest_folder = "Misc" # Default folder for unknown types
        for folder, extensions in file_types.items():
            if extension in extensions:
                dest_folder = folder
                break

        # Attempt to move the file
        try:
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            shutil.move(file, os.path.join(dest_folder, file))
            print(f"✅ Moved: {file} -> {dest_folder}/")

        except shutil.Error:
            print(f"⚠️  Skipped: {file} already exists in {dest_folder}/")
        except PermissionError:
            print(f"❌ Error: Permission denied. Is '{file}' currently open?")
        except Exception as e:
            print(f"❗ An unexpected error occurred with {file}: {e}")

if __name__ == "__main__":
    # Replace this with the path to the folder you want to organize
    print("Digi-Maid: Your Digital Cleaning Assistant")
    path_to_clean = input("Enter the full path of the folder to organize: ")
    organize_folder(path_to_clean)