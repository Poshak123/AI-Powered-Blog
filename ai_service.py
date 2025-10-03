import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content(prompt: str, max_tokens: int = 300) -> str:
    """
    Call OpenAI API to generate content based on prompt.
    """
    if not client.api_key:
        return "OpenAI API key not configured."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # updated model for newer API
            messages=[
                {"role": "system", "content": "You are a helpful assistant for generating blog content."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating content: {e}"
