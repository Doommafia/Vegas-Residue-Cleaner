import os

def VegasResidueCleaner(rootFolder):
    for root, dirs, files in os.walk(rootFolder):
        for file in files:
            # Check if the file ends with ".sfk"
            if file.endswith(".sfk"):
                # Construct the corresponding .mp4 file name
                mp4File = os.path.splitext(file)[0] + ".mp4"

                # Delete the .sfk file
                sfkPath = os.path.join(root, file)
                print("File ", sfkPath, ' deleted!\n' )
                os.remove(sfkPath)

                # Delete the corresponding .mp4 file if it exists
                mp4Path = os.path.join(root, mp4File)
                if os.path.exists(mp4Path):
                    os.remove(mp4Path)

    print("SFK and MP4 files deleted successfully!")

#Define your folder
rootFolder = "D:\Videos"
VegasResidueCleaner(rootFolder)
