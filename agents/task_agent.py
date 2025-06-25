# agents/task_agent.py

import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI

# Load environment variables from .env
load_dotenv()

def run_agent():
    # Check if API key is loaded correctly
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY not found. Please set it in your .env file or pass it as an environment variable.")

    # Prompt template
    prompt = PromptTemplate(
        input_variables=["user_input"],
        template="You are a helpful assistant. User said: {user_input}\nHow do you respond?"
    )

    # Initialize the LLM (uses OPENAI_API_KEY from env)
    llm = OpenAI(temperature=0.7)

    # Create the chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Chat loop
    print("🤖 LangChain Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        response = chain.run(user_input=user_input)
        print(f"Chatbot: {response}")
