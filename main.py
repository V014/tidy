import os
import shutil
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Initialize the main application window
root = ttk.Window()
# Set window title
root.title("Digi-Maid")
# Set window size
root.geometry("400x300")
# Set window theme
style = ttk.Style("superhero")

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

    # Define the names of folders the script creates so it doesn't move them!
    protected_folders = list(file_types.keys()) + ["Misc", "Sorted_Folders"]

    try:
        os.chdir(target_path)
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
        return

    for item in os.listdir():
        # --- FOLDER LOGIC ---
        if os.path.isdir(item):
            # Skip if it's one of our organization folders
            if item in protected_folders:
                continue
            
            try:
                if not os.path.exists("Sorted_Folders"):
                    os.makedirs("Sorted_Folders")
                
                shutil.move(item, os.path.join("Sorted_Folders", item))
                print(f"📂 Moved Folder: {item} -> Sorted_Folders/")
            except Exception as e:
                print(f"❌ Could not move folder {item}: {e}")
            continue # Move to next item

        # --- FILE LOGIC ---
        name, extension = os.path.splitext(item)
        extension = extension.lower()

        dest_folder = "Misc"
        for folder, extensions in file_types.items():
            if extension in extensions:
                dest_folder = folder
                break

        try:
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            shutil.move(item, os.path.join(dest_folder, item))
            print(f"📄 Moved File: {item} -> {dest_folder}/")
        except shutil.Error:
            print(f"⚠️  Skipped: {item} already exists.")
        except Exception as e:
            print(f"❗ Error with {item}: {e}")

if __name__ == "__main__":
    # Replace this with the path to the folder you want to organize
    print("Digi-Maid: Your Digital Cleaning Assistant")
    path_to_clean = input("Enter the full path of the folder to organize: ")
    organize_folder(path_to_clean)



# Start the GUI event loop
root.mainloop()