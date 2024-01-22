from dotenv import load_dotenv
import google.generativeai as genai
import os
import requests
import io

load_dotenv('.env.local')

genai.configure(api_key=os.getenv('GENAI_API_KEY'))

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

POEM = "Write a poem about a "

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

def generate_image(image_description):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}

    def query(payload):
      response = requests.post(API_URL, headers=headers, json=payload)
      return response.content
    
    image_bytes = query({
      "inputs": image_description,
    })

    return io.BytesIO(image_bytes)

def generate_text(topic, type):
    response = model.generate_content(type + topic)
    return response.text
