from dotenv import load_dotenv
import google.generativeai as genai
import os
import requests
import io
import json
import logging

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

POEM = "poem"
STORY = "story"

metaprompt = """
Output the following JSON format 
{{
    "text": "# prompt for {type}",
    "title": "# title of the {type}",
	"image": "# prompt for generating image"
}}

for the given topic {topic}

for example topic: 'a rabbit and a turtle'
output:
{{
    "text": "write a {type} about a rabbit and a turtle racing against each other, and unexpectedly the turtle wins",
    "title": "The Race of Rabit and Turtle",
    "image": "create an image consisting a rabbit and turtle running towards a finish line"
}}
"""

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

    logging.info(f"generated image: {image_description}")
    return io.BytesIO(image_bytes)

def generate_text(prompt):
    response = model.generate_content(prompt)
    logging.info(f"generated text: {prompt}")
    return response.text

def generate_metadata(topic, type):
    prompt = metaprompt.format(type=type, topic=topic)
    response = model.generate_content(prompt)
    data = json.loads(response.text)

    logging.info(f"generated metadata: {data}")

    return data
