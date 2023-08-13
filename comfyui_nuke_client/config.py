"""
Juno Innovations

ComfyUI configuration settings.
"""

COMFYUI_ROOT = None
COMFYUI_HOST = 'http://localhost:8188'


def set_root(path):
    """
    Set the root path for ComfyUI.
    """
    global COMFYUI_ROOT
    COMFYUI_ROOT = path


def set_host(url):
    """
    Set the host for ComfyUI.
    """
    global COMFYUI_HOST
    COMFYUI_HOST = url


def get_host():
    """
    Get the host for ComfyUI.
    """
    return COMFYUI_HOST


def get_output_path():
    """
    Get the output path for ComfyUI.
    """
    return f'{COMFYUI_ROOT}/output/'
