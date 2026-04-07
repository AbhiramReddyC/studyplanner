from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

# Initialize Groq model
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="openai/gpt-oss-20b"  # Supported model
)

# Ask user for subjects
query = input("Enter subjects you want to study: ")

# Create prompt
prompt = f"""
Create a 7 day study plan for the following subjects:
{query}

Include daily topics and revision.
"""

# Generate response
response = llm.invoke(prompt)

# Print the personalized study plan
print("\nYour Personalized Study Plan:\n")
print(response.content)
