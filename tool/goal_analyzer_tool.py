from openai import AsyncOpenAI
from agents import function_tool
from typing import TypedDict

class GoalInput(TypedDict):
    user_message: str

class AnalyzedGoal(TypedDict):
    goal_type: str  # e.g., weight_loss, muscle_gain, recovery
    diet_preference: str  # e.g., vegetarian, keto, no_pref
    duration_days: int

@function_tool()
def goal_analyzer_tool(input: GoalInput) -> AnalyzedGoal:
    """Analyze user's fitness and dietary goals from natural language input."""
    message = input["user_message"].lower()

    goal_type = "general_fitness"
    if "lose weight" in message or "fat loss" in message:
        goal_type = "weight_loss"
    elif "gain muscle" in message:
        goal_type = "muscle_gain"
    elif "injury" in message or "recover" in message:
        goal_type = "recovery"

    if "vegetarian" in message:
        diet = "vegetarian"
    elif "keto" in message:
        diet = "keto"
    else:
        diet = "no_pref"

    duration = 7 if "week" in message or "7 days" in message else 5

    return {
        "goal_type": goal_type,
        "diet_preference": diet,
        "duration_days": duration
    }
