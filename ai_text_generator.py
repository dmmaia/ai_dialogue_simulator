from google import genai
from google.genai import types

client = genai.Client()

def generateResponse(content):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=content,
        config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
    )
    return response.text