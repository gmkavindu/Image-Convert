from PIL import Image
import os

output_folder = '/opt/icons/'
os.makedirs(output_folder, exist_ok=True)
images_directory = '/images'

for filename in os.listdir(images_directory):
    image_path = os.path.join(images_directory, filename)
    
    img = Image.open(image_path)
    img = img.convert("RGB")
    img = img.rotate(-90)
    img = img.resize((128, 128))
    
    f, e = os.path.splitext(filename)
    outfile = f + ".jpeg"
    if filename != outfile:
        try:
            img.save(os.path.join(output_folder,outfile))
        except OSError as e:
            print("cannot convert", filename)
            print("Error:", e)

    
