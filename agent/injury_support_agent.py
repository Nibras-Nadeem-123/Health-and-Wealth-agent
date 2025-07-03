from agents import Agent, OpenAIChatCompletionsModel
from tool.workout_plan_generator_tool import workout_plan_generator_tool
from openai import AsyncOpenAI
import os

injury_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)


def injury_support_agent():
    return Agent(
        name="Injury Support Assistant",
        instructions=(
            "You are a physical therapist AI assistant. "
            "Your job is to help users with injuries adjust their workout plans. "
            "If the user mentions an injury (e.g., knee, back), modify the plan accordingly. "
            "Use the workout_plan_generator_tool and provide gentle, safe alternatives. "
            "Use a compassionate tone. Don't recommend anything unsafe."
        ),
        model=OpenAIChatCompletionsModel(
            model="gemini-1.5-flash",
            openai_client=injury_client
        ),
        tools=[workout_plan_generator_tool]
    )
