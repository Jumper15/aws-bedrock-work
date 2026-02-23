from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

response = client.responses.create(
     model="openai.gpt-oss-120b",
     input="What is aws bedrock"
)

print(response)