"""
Juno Innovations
"""
# std
import os
from typing import List, Dict

# 3rd
import requests

# local
from .logger import LOGGER
from .config import get_output_path, get_host


def verify_connection() -> bool:
    """
    Verify connection to the server
    """
    try:
        LOGGER.info("Verifying connection to the server.")
        stats = system_stats()
        LOGGER.info("ComfyUI server is running.")
        LOGGER.info(f'Devices: {[x["name"] for x in stats["devices"]]}')
        LOGGER.info('ComfyUI good to go.')
        return True
    except requests.exceptions.ConnectionError:
        LOGGER.warning("ComfyUI server is not running.")
        return False


def system_stats() -> Dict:
    """
    Get system stats
    """
    url = f'{get_host()}/system_stats'

    response = requests.get(url)
    return response.json()


def upload_image(image_path) -> Dict:
    """
    Upload an image to comfy
    """
    url = f'{get_host()}/upload/image'

    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(url, files=files)
    return response.json()


def upload_mask(image_path) -> Dict:
    """
    Upload an image as a mask to comfy
    """
    url = f'{get_host()}/upload/mask'

    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(url, files=files)
    return response.json()


def output_images() -> List[str]:
    """
    Get the output images
    """
    # list all files based on newest to oldest

    images = []
    output_path = get_output_path()
    for img in os.listdir(output_path):
        images.append(os.path.join(output_path, img))

    images.sort(key=os.path.getmtime, reverse=True)

    return [os.path.basename(x) for x in images]
