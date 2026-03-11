# ============== IMAGE GENERATOR ==============
import openai
import requests
import os
import random
from datetime import datetime
from config import OPENAI_API_KEY, IMAGE_FOLDER, USE_AI_IMAGES
from post_generator import generate_image_prompt

openai.api_key = OPENAI_API_KEY

# Ensure image folder exists
os.makedirs(IMAGE_FOLDER, exist_ok=True)


def generate_ai_image(post_content):
    """DALL-E se professional image generate karo"""
    
    try:
        image_prompt = generate_image_prompt(post_content)
        print(f"🎨 Image Prompt: {image_prompt[:100]}...")
        
        response = openai.Image.create(
            model="dall-e-3",
            prompt=image_prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        
        image_url = response.data[0].url
        
        # Image download karo
        img_response = requests.get(image_url)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{IMAGE_FOLDER}/post_{timestamp}.png"
        
        with open(filename, "wb") as f:
            f.write(img_response.content)
        
        print(f"✅ Image saved: {filename}")
        return filename
        
    except Exception as e:
        print(f"❌ AI Image generation failed: {e}")
        return get_local_image()


def get_local_image():
    """Local folder se random image uthao"""
    
    try:
        images = [f for f in os.listdir(IMAGE_FOLDER) 
                  if f.endswith(('.png', '.jpg', '.jpeg', '.webp'))]
        
        if images:
            selected = random.choice(images)
            filepath = os.path.join(IMAGE_FOLDER, selected)
            print(f"📁 Using local image: {filepath}")
            return filepath
        else:
            print("⚠️ No local images found!")
            return None
            
    except Exception as e:
        print(f"❌ Error loading local image: {e}")
        return None


def get_image_for_post(post_content):
    """Post ke liye image lao — AI ya local"""
    
    if USE_AI_IMAGES:
        return generate_ai_image(post_content)
    else:
        return get_local_image()