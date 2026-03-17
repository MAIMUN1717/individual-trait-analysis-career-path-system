import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Get API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model name
MODEL_NAME = "llama-3.3-70b-versatile"

# Create Groq client
client = Groq(
    api_key=GROQ_API_KEY
)

# ✅ ADD THIS LINE (VERY IMPORTANT)
groq_client = client