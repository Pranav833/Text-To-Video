from diffusers import DiffusionPipeline 
import torch

pipe = DiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    use_safetensors=True,
)

image = pipe("cry",width=512, height=512, num_inference_steps=5).images[0]
image.save('generatedimage1.png')
image = pipe("wolf",width=512, height=512, num_inference_steps=5).images[0]
image.save('generatedimage2.png')
print('done')