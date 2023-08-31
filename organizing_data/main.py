import os
import shutil

# Replace these paths with the actual paths
source_dataset_path = 'C:/Users/ASUS/Desktop/cars - Copie'
destination_dataset_path = 'C:/Users/ASUS/Desktop/training'

# Get a list of all image files in the source dataset directory
image_files = [f for f in os.listdir(source_dataset_path) if f.endswith('.jpg') or f.endswith('.png')]

# Create a dictionary to store class and subclass information
class_subclass_mapping = {}

# Extract class and subclass information from image filenames
for image_file in image_files:
    parts = image_file.split('_')
    car_class = parts[0]
    car_subclass = parts[1]
    class_subclass_mapping.setdefault(car_class, set()).add(car_subclass)

# Create the desired directory structure in the destination dataset
for car_class, subclasses in class_subclass_mapping.items():
    class_dir = os.path.join(destination_dataset_path, car_class)
    os.makedirs(class_dir, exist_ok=True)
    for subclass in subclasses:
        subclass_dir = os.path.join(class_dir, subclass)
        os.makedirs(subclass_dir, exist_ok=True)

# Copy images to the appropriate subclass folders in the destination dataset
for image_file in image_files:
    parts = image_file.split('_')
    car_class = parts[0]
    car_subclass = parts[1]
    source_path = os.path.join(source_dataset_path, image_file)
    destination_path = os.path.join(destination_dataset_path, car_class, car_subclass, image_file)
    shutil.copy(source_path, destination_path)

print("Dataset copied and organized successfully.")
