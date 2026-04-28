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
 
chat_history =[]
 
print("Chat Assitant Ready! type 'by' or 'exit' to stop. \n")
 
while True:
    ux_input = input('You:'.strip())
    print('\n')
    if ux_input.lower() in ['bye', 'exit']:
        print('Assistant 🤖: Goodbye 👋')
 
    messages = chat_history + [{'role':'user', 'content':ux_input}]
    result = agent.invoke({'messages':messages})
 
    try:
        reply = result['messages'][-1].content
    except Exception as e:
        reply = str(e)
 
    
    print(f'Assistant 🤖: {reply} \n')
    print('-'*60)
 
    #update chat history
    chat_history.append({'role': 'user', 'content':'user_input'})
    chat_history.append({'role':'assistant', 'content':'reply'})
 