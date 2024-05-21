from diffusers import StableDiffusionPipeline
import torch
import warnings

# Load the pre-trained Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"

# Load the model checkpoint into the pipeline
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, low_cpu_mem_usage=True)

# Move the pipeline to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

warnings.filterwarnings("ignore", message="1Torch was not compiled with flash attention.") # Optional

def generate_image(prompt: str):
    # Generate image from the prompt
    image = pipe(prompt).images[0]

    # Implement NSFW / https://github.com/GantMan/nsfw_model

    return image


