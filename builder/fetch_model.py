"""
Downloads the model to cache.
"""

from lavis.models import load_model_and_preprocess

load_model_and_preprocess(name="blip_caption", model_type="base_coco", is_eval=True, device="cpu")
