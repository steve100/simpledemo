# environment
#AZURE_OPENAI_ENDPOINT=https://<your-resource-name>.openai.azure.com
#AZURE_OPENAI_API_KEY=<your-azure-key>
#AZURE_OPENAI_DEPLOYMENT=<your-deployment-name>  # e.g., gpt-4o-mini or your custom deployment name


from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

chat = client.chat.completions.create(
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"],  # deployment name in Azure
    messages=[{"role":"user","content":"Hello from Azure OpenAI via Python!"}]
)
print(chat.choices[0].message.content)