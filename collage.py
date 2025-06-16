import os
from PIL import Image
import math

image_folder = 'images' # папка с фото
output_image = 'collage.png' # как будет называться файл отпут
image_dimension = 400 # масштаб фото (к примеру тут стоит 400x400)
border_width = 1 
block_dimension = image_dimension + 2 * border_width
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
num_images = len(image_files)

if num_images == 0:
    print("нет изображений для создания коллажа")
else:
    side_count = math.ceil(math.sqrt(num_images))
    collage_dimension = side_count * block_dimension
    collage = Image.new('RGB', (collage_dimension, collage_dimension))
    x, y = 0, 0
    for image_file in image_files:
        img_path = os.path.join(image_folder, image_file)
        try:
            img = Image.open(img_path)
            img = img.convert('RGBA')
            img = img.convert('RGB')
            img = img.resize((image_dimension, image_dimension), Image.LANCZOS)
            bordered_img = Image.new('RGB', (block_dimension, block_dimension), color='white')
            bordered_img.paste(img, (border_width, border_width))
            collage.paste(bordered_img, (x, y))
            x += block_dimension
            if x >= collage_dimension:
                x = 0
                y += block_dimension
        except Exception as e:
            print(f"ошибка с файлом {img_path}: {e}")
    collage.save(output_image)
    print(f"коллаж успешно сохранён как {output_image}")
