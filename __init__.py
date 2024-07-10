from .custom_nodes.ComfyUINetCLIPSegNodes import ComfyUINetCLIPSeg, ComfyUINetombineMasks

NODE_CLASS_MAPPINGS = {
    "ComfyUINetCLIPSeg": ComfyUINetCLIPSeg,
    "ComfyUINetombineMasks": ComfyUINetombineMasks,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUINetCLIPSeg": "ComfyUI.Net CLIPSeg",
    "ComfyUINetombineMasks": "ComfyUI.Net Combine Masks",
}