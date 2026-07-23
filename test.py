import os
from dotenv import load_dotenv
from google import genai

# 1. Load secret API Key from .env
load_dotenv()

# 2. Initialize client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 3. Call Gemini using an active model from your list
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Say hello in one sentence."
)

# 4. Print response
print(response.text)