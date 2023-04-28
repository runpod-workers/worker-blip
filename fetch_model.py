from lavis.models import load_model_and_preprocess

# Set up the device
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

load_model_and_preprocess(
    name="blip_caption", model_type="base_coco", is_eval=True, device=DEVICE
)
