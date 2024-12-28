import os
from PIL import Image

image_folder = 'photo'  # создадите папку под этим названием и закиньте туда фото
output_image = 'collage.jpg'
collage_width = 1000  # ширина фото
collage_height = 1000  # длина фото
thumbnail_size = 100  # размер фото в коллаже (оно будет в виде квадрата к примеру 100x100)
thumbnails_per_row = collage_width // thumbnail_size
thumbnails_per_column = collage_height // thumbnail_size
collage = Image.new('RGB', (collage_width, collage_height))
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
image_files = image_files[:1000]  # максимум фото задаётся здесь
x, y = 0, 0

for idx, image_file in enumerate(image_files):
    img_path = os.path.join(image_folder, image_file)
    try:
        img = Image.open(img_path)
        img.thumbnail((thumbnail_size, thumbnail_size))
        collage.paste(img, (x, y))
        x += thumbnail_size
        if x >= collage_width:
            x = 0
            y += thumbnail_size
        if idx >= 999:  # тут нужно просто от максимального количество фото отнять 1
            break
    except Exception as e:
        print(f"ошибка с файлом {img_path}: {e}")

collage.save(output_image)
print(f"коллаж успешно сохранён как {output_image}")
