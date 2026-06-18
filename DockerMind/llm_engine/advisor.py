from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise Exception(
        "GROQ_API_KEY not found. Run: export GROQ_API_KEY='your_key'"
    )

# Initialize Groq client
client = Groq(
    api_key=api_key
)


def get_recommendation(issue, log_text):

    prompt = f"""
You are a Kubernetes Site Reliability Engineer.

Issue Type:
{issue}

Container Log:
{log_text}

Provide:

1. Root Cause
2. Troubleshooting Steps
3. Prevention Strategy

Keep the response concise and practical.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content


# Local Testing
if __name__ == "__main__":

    result = get_recommendation(
        "database timeout",
        "Database connection timeout after 30 seconds"
    )

    print(result)