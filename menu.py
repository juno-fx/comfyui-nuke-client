"""
Juno Innovations

ComfyUI Nuke Client

ONLY FOR DEVELOPMENT

It is expected that your pipeline team would install this package for you. This is only an example.
"""
# std
import os

# 3rd
import nuke

# add the requirements path.
nuke.pluginAddPath('./requirements')

# import the client
import comfyui_nuke_client

# configure the root path for ComfyUI, mine is installed in my home directory
comfyui_nuke_client.config.set_root(os.path.expanduser('~/ComfyUI'))


# menu configuration
menu = nuke.menu('Nuke')
menu.addCommand('ComfyUI/Open in Browser', comfyui_nuke_client.open_comfy)
menu.addSeparator()
menu.addCommand('ComfyUI/Import', comfyui_nuke_client.import_from_comfy)
menu.addCommand('ComfyUI/Export Image', comfyui_nuke_client.export_image)
