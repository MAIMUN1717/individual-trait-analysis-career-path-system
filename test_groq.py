import os
from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ GROQ_API_KEY not found in .env")
    exit()

print("✅ API key loaded")

try:
    client = Groq(api_key=api_key)

    print("🚀 Sending test request to Groq...")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Explain artificial intelligence in one sentence."
            }
        ],
        temperature=0.3
    )

    print("\n✅ GROQ RESPONSE:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print("\n❌ GROQ CONNECTION FAILED")
    print(e)