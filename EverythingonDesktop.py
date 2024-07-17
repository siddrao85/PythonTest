import os
import shutil

source_dir = '/Users/siddh/Desktop'
base_destination_dir = '/Users/Siddh/Desktop/Everything'

# Create a unique destination directory
i = 1
destination_dir = base_destination_dir
while os.path.exists(destination_dir):
    destination_dir = f"{base_destination_dir}{i}"
    i += 1

os.makedirs(destination_dir)

# Get the name of the current script
current_script = os.path.basename(__file__)

# Move files
for item in os.listdir(source_dir):
    source_path = os.path.join(source_dir, item)

    # Skip the current script and the destination directory
    if item == current_script or item == os.path.basename(destination_dir):
        continue

    # Check if it's a file (not a directory)
    if os.path.isfile(source_path):
        try:
            shutil.move(source_path, destination_dir)
            print(f"Moved: {item}")
        except Exception as e:
            print(f"Error moving {item}: {str(e)}")

print(f"Files moved to: {destination_dir}")