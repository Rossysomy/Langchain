import os
from dotenv import load_dotenv
 
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
 
load_dotenv()
 
api_key = os.getenv("GEMINI_API_KEY")
 
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature = 0
)
 
agent = create_agent(
    model = model,
    tools = [],
    system_prompt = "You are a helpful chat assistant. Be clear, concise and polite. "\
          "Understand the user's intent and respond politely. Stay professional and safe. "
)
 
 
result = agent.invoke(
    {
        "messages": [{"role":"user","content":"Explain Machine Learning in Short."}]
    }
)
 
print(result['messages'][1].content)