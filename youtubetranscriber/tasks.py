from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer
from dotenv import load_dotenv
load_dotenv()
#research task

research_task=Task(
    description=(
        "Identify the video {topic}"
        "Get detailed information about the video from the channel"
    ),
    expected_output='A comprehensive 3 paragraph long report based on the {topic} of the video",
    tools=[yt_tool],
    agent=blog_researcher
)

# writer task

write_task=Task(
    description=(
        "Get the info from the youtube channel on the topic {topic}"
    ),
    expected_output="Summarize the info from the youtube channel video on the topic {topic}",
    tools=[yt_tool],
    async_execution=False,     
    agent=blog_writer,
    output_file='new-blog-post.md'
)

    
