import os

def VegasResidueCleaner(rootFolder):
    for root, dirs, files in os.walk(rootFolder):
        for file in files:
            if file.endswith(".mp4"):
                mp4_file_path = os.path.join(root, file)
                sfk_file_path = os.path.join(root, file + ".sfk")
                
                if os.path.exists(sfk_file_path):
                    print("\n")
                    os.remove(mp4_file_path)
                    print(f"{file} has been deleted.")
                    
                    os.remove(sfk_file_path)
                    print(f"{file}.sfk has been deleted.")

    print("MP4 files and corresponding MP4.SFK files deleted successfully!")

# Define your folder
rootFolder = "C:/Videos"
VegasResidueCleaner(rootFolder)
