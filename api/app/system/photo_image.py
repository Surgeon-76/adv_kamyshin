import datetime
import os
from PIL import Image
from fastapi import UploadFile


def check_folder(path_folder: str):
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)


def image_add_origin(image: UploadFile):
    data = str(datetime.datetime.now()).replace(" ", "")
    image = Image.open(image.file)
    new_width = new_height = 1080
    quality = 100
    width, height = image.size

    if height > width:
        new_width = int(new_height * width / height)
    elif width > height:
        new_height = int(new_width * height / width)

    image = image.resize((new_width, new_height))
    path_image = f'static/images/origin/{data}.webp'
    image.save(path_image, format="WebP", quality=quality, optimize=True)
    return path_image


def image_add(image: UploadFile, path_image: str):
    data = str(datetime.datetime.now()).replace(" ", "")
    image = Image.open(image.file)
    new_width = new_height = 150
    quality = 30
    width, height = image.size

    if height > width:
        new_width = int(new_height * width / height)
    elif width > height:
        new_height = int(new_width * height / width)

    image = image.resize((new_width, new_height))
    # path_image = 'static/images/logo/'
    check_folder(path_image)
    path_image += f'{data}.webp'
    image.save(path_image, format="WebP", quality=quality, optimize=True)
    return path_image


def image_delete(path_image: str, path_image_tumb: str = ''):
    if os.path.isfile(path_image):
        os.remove(path_image)
    if os.path.isfile(path_image_tumb):
        os.remove(path_image_tumb)
