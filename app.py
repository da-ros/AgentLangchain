import requests
import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun

# Load the environment variables from the .env file
load_dotenv()
# Get the environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Initialize the ChatOpenAI client with the API key
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    temperature=0.8,
    model_name="gpt-3.5-turbo"
)

# Define the prompt template
prompt = PromptTemplate(
  input_variables=["query"],
  template="You are New Native Internal Bot. Help users with their important tasks, like a professor in a particular field. Query: {query}"
)

# Initialize the LLMChain
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
response = llm_chain.run("What is lablab.ai")
print(response)
response = llm_chain.run("Integral of x * (log(x)^2)")
print(response)


# Prepare Tools for Agent
# Resolve the issue of outdated and wrong answers with DuckDuckGo web search and Wolfram Alpha API
search = DuckDuckGoSearchRun()

# Web Search Tool
search_tool = Tool(
    name = "Web Search",
    func=search.run,
    description="A useful tool for searching the Internet to find information on world events, issues, etc. Worth using for general topics. Use precise questions."
)

# Wolfram Alpha class
class WA:
  """
    Wolfram|Alpha API
  """
  def __init__(self, app_id):
    self.url = f"http://api.wolframalpha.com/v1/result?appid={app_id}&i="

  def run(self, query):
    query = query.replace("+", " plus ").replace("-", " minus ") # '+' and '-' are used in URI and cannot be used in request
    result = requests.post(f"{self.url}{query}")

    if not result.ok:
      raise Exception("Cannot call WA API.")

    return result.text
  

WA_API_KEY = os.getenv("WA_API_KEY") # You can get it here: https://products.wolframalpha.com/api/

wa = WA(app_id=WA_API_KEY)

wa_tool = Tool(
    name="Wolfram|Alpha API",
    func=wa.run,
    description="Wolfram|Alpha API. It's super powerful Math tool. Use it for simple & complex math tasks."
)

# Create Agent and test performance
agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=[wa_tool, search_tool],
    llm=llm,
    verbose=True, # I will use verbose=True to check process of choosing tool by Agent
    max_iterations=3
)

# Let's check out previous prompts!
r_1 = agent("What is lablab.ai?")
print(f"Final answer: {r_1['output']}")

r_2 = agent("Integral of x * (log(x)^2)")
print(f"Final answer: {r_2['output']}")