import google.generativeai as genai
from PIL import Image

def init_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("models/gemini-2.5-flash")  # ✅ Use updated model name

def generate_caption(model, image_file, user_prompt=""):
    try:
        image = Image.open(image_file)

        # Default caption instruction
        base_prompt = "Describe this image for social media."

        # Combine prompts if user gives input
        if user_prompt:
            full_prompt = f"{base_prompt} Style: {user_prompt}"
        else:
            full_prompt = base_prompt

        response = model.generate_content([full_prompt, image])
        return response.text.strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
