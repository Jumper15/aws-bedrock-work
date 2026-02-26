from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
     model="bedrock/anthropic. anthropic.claude-3-5-sonnet-20241022-v2:0",
     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
     aws_region_name=os.getenv('AWS_REGION_NAME')
)

@CrewBase
class DevelopmentCrew():
     agents: List[BaseAgent] # self.agents type annotation
     tasks: List[Task] # self.tasks type annotation
     
     @agent
     def researcher(self) -> Agent:
          
     