from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["OPENAI_API_KEY"]="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"
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"
llm=ChatGoogleGenerativeAI(model="gemini-pro",
                           verbose=True,
                           temperature=0.5,
                           google_api_key='AIzaSyCG9qaINdEYyfukj04JBQwXeP_PH0wEo_w'
                          )

#create a Senior blog content researcher
blog_researcher=Agent(
    role="""Blog Researcher from youtube videos""",
    goal="""get the relevant video content for the topic
    {topic} from the youtube channel
    """,
    verbose=True,
    memory=True,
    backstory=(
   """ This agent is an expert in 
   understanding videos in AI/ML/Gen AI .etc
   """
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

## Creating a senior blog writer agent with YT tool
blog_writer=Agent(
    role="Writer",
    goal="Narrate compelling tech stories about the video{topic}",
    verbose=True,
    memory=True,
    backstory=(
        """ With a flair of simplifying complex topics, you craft
        engaging narratives that captivate and educate, bringing 
        new discoveries to light in an accessible manner"""
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=False

)
