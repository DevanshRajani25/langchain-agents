import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

@tool('get_weather', description='Return weather information in short for a given city')
def get_weather(city: str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

agent = create_agent(
    model = 'gpt-4o',
    tools = [get_weather],
    system_prompt = 'You are very helpful weather assistant, which gives answer to user query related to weather very politely.'
)

response = agent.invoke({
    'messages': [
        {'role': 'user', 'content': 'What is the weather of Rajkot today?'}
    ]
})

print(response['messages'][-1].content)