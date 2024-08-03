from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
from dotenv import load_dotenv
load_dotenv()
#forming the crew
crew=Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

#start execution of crew with feedback
result=crew.kickoff(inputs={'topic': "What are the best stocks to buy?"})
print(result)
