from crewai import Agent
from tools import yt_tool

from load_dotenv import load_dotenv

import os
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME']="gpt-3.5-turbo-0125"


### Create a senior blog content  researcher

blog_researcher = Agent(

    role="Blog Researcher from Youtube Videos",
    goal="get the releveant video content for the topis{topis} from yt channel",
    verbose= True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and GENAI providig suggestions"

    ),
    tools= [yt_tool],
    allow_delegation= True



)


# Creating the senior blog writer agent with yt tool

blog_writer=Agent(
    role="Writer",
    goal="Narrate compelling tech stories about the video {topis} from YT channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you creaft"
        "Engaging narratives that captivate and educate, bringing new"
        "Discoveries to light in an accessible manner."

    ),
    tools=[yt_tool],
    allow_delegation=False
)