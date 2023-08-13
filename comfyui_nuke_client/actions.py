"""
Juno Innovations

Handles all actions that can be run within Nuke to interact with the ComfyUI
"""
# std
import os

# 3rd party
import nuke

# local
from .connection import upload_image, output_images, upload_mask
from . import config


SUPPORTED_FILE_TYPES = ['jpeg', 'png']


def send_to_comfy():
    """
    Sends a Write nodes resulting image to ComfyUI
    """
    try:
        selected = nuke.selectedNode()
    except ValueError:
        nuke.message("No node selected")
        return

    if selected.Class() != "Write":
        nuke.message("Selected node is not a Write node")
        return

    file_type = selected["file_type"].value()
    if file_type not in SUPPORTED_FILE_TYPES:
        nuke.message(f"Image must on of the following: {SUPPORTED_FILE_TYPES}")
        return

    path = selected["file"].value()
    if not os.path.exists(path):
        nuke.message("File does not exist, please render the image first")
        return

    return selected["file"].value()


def export_image():
    """
    Sends a Write nodes resulting image to ComfyUI
    """

    path = send_to_comfy()
    if not path:
        return

    # send to comfy
    upload_image(path)


def import_from_comfy():
    """
    Imports a file from ComfyUI
    """
    outputs = output_images()
    choice = nuke.choice(
        "Nuke ComfyUI",
        "Import image from Comfy",
        outputs
    )

    if choice is None:
        return

    nuke.nodes.Read(file=os.path.join(config.get_output_path(), outputs[choice]))


def open_comfy():
    """
    Open the ComfyUI in the browser
    """
    os.system(f"xdg-open {config.get_host()}")
