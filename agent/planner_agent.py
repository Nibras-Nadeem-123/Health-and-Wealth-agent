from agents import Agent, OpenAIChatCompletionsModel
from tool.goal_analyzer_tool import goal_analyzer_tool
from tool.meal_plan_generator_tool import meal_plan_generator_tool
from tool.workout_plan_generator_tool import workout_plan_generator_tool
from agent.injury_support_agent import injury_support_agent 
from agent.injury_support_agent import injury_support_agent
from openai import AsyncOpenAI
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

gemini_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Enhanced planner with memory-aware instructions

def planner_agent() -> Agent:
    return Agent(
        name="Health & Wellness Planner",
        instructions=(
            "You are a certified health planner. "
            "Collect user goals, generate plans, and stream responses. "
            "If the user mentions an injury (e.g., 'knee pain', 'back injury', etc), "
            "perform a handoff to the Injury Support Agent. "
            "Use tools only when needed. Track memory in state."
        ),
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash-lite",
            openai_client=gemini_client,
        ),
        tools=[
            goal_analyzer_tool,
            meal_plan_generator_tool,
            workout_plan_generator_tool,
        ],
        handoffs=[injury_support_agent()]
    )

