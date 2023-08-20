import datetime
import os
from PIL import Image


async def image_add(image):
    data = str(datetime.datetime.now()).replace(" ", "")
    image = Image.open(image.file)
    width, height = image.size
    new_width = 250
    new_height = int(new_width * height / width)
    image = image.resize((new_width, new_height))
    path_image = f'static/images/{data}.webp'
    image.save(path_image, format="WebP", quality=50, optimize=True)
    return path_image


async def image_add_origin(image):
    data = str(datetime.datetime.now()).replace(" ", "")
    image = Image.open(image.file)
    # image = image.resize((1920, 1080))
    path_image = f'static/images/{data}.webp'
    image.save(path_image, format="WebP", quality=100, optimize=True)
    return path_image


async def image_delete(path_image: str, path_image_tumb: str):
    return (os.remove(path_image),
            os.remove(path_image_tumb))
