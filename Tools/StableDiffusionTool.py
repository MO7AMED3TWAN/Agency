# Stable Diffusion Tool
from transformers import pipeline

class StableDiffusionTool:
    def __init__(self):
        self.generator = pipeline('text-to-image', model='CompVis/stable-diffusion-v1-4', revision='fp16', torch_dtype='float16')

    def generate_image(self, prompt):
        return self.generator(prompt)
