#from dotenv import load_dotenv
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env
# this is a better way however using environment varable for the key for now.
# ollama and lm studio do not need a key
# Load variables from .env file
load_dotenv()

# Get the API key from the encironment .. or the .env if we call load_dotenv() 
api_key = os.getenv("OPENAI_API_KEY")

# Get your key from the environment
api_key = os.getenv("OPENAI_API_KEY")

#pull in model type
import sys

# sys.argv[0] is the script name itself
# sys.argv[1:] are the arguments

print("Arguments:", sys.argv[1])

if len(sys.argv) == 2:
    llm = sys.argv[1]
else:
    llm = "local"   

# if you do not specifiy a location, it will be local
print(llm)

#llm="openai"
#llm="local"

if (llm=="local"):
# Set the Ollama endpoint (local)
   
    client = OpenAI(
        base_url="http://localhost:11434/v1"  # Ollama's API endpoint
        #api_key="ollama",  # dummy key required by the client # actually maybe not needed
    )
    model = "llama3"        # did not use to need this  
    
elif (llm=="openai"):
# Initialize client
    client = OpenAI(api_key=api_key)
    model = "gpt-4o-mini"

else: 
    print("error: python3 simple.py llm|openai")
    exit(1) 

# Send a simple prompt to a local model, e.g. "llama3" or "qwen2"
# old way client.chat.completions.create  new way client.responses.create
# ChatGPT suggests continue to use old way.  

response = client.chat.completions.create( 
    model=model,  # see above if statement for local vs openai
    messages=[
        {"role": "user", "content": "Write a haiku about sunrise"}
    ]
)

print(response.choices[0].message.content)

# Micrsoft new way works with openapi but not local
#response = client.responses.create(
#    model=model,
#    input="Write a haiku about Node.js"
#)
#
#print(response.output[0].content[0].text)


