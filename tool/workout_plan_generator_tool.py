from agents import function_tool
from typing import TypedDict, List, Dict

class WorkoutPlanInput(TypedDict):
    goal_type: str         # e.g., weight_loss, muscle_gain, recovery
    duration_days: int     # e.g., 5 or 7

class DailyWorkout(TypedDict):
    workout: str
    duration: str
    focus_area: str

class WorkoutPlanOutput(TypedDict):
    plan: List[DailyWorkout]

@function_tool()
def workout_plan_generator_tool(input: WorkoutPlanInput) -> WorkoutPlanOutput:
    """Generates a personalized workout plan based on the user's goal."""

    goal = input["goal_type"]
    days = input["duration_days"]

    weight_loss_plan = [
        {"workout": "HIIT Cardio", "duration": "30 mins", "focus_area": "Full Body"},
        {"workout": "Jogging", "duration": "40 mins", "focus_area": "Lower Body"},
        {"workout": "Bodyweight Circuit", "duration": "30 mins", "focus_area": "Core & Legs"},
    ]

    muscle_gain_plan = [
        {"workout": "Push Day (Chest, Shoulders, Triceps)", "duration": "45 mins", "focus_area": "Upper Body"},
        {"workout": "Pull Day (Back, Biceps)", "duration": "45 mins", "focus_area": "Upper Body"},
        {"workout": "Leg Day", "duration": "50 mins", "focus_area": "Lower Body"},
    ]

    recovery_plan = [
        {"workout": "Stretching + Light Yoga", "duration": "20 mins", "focus_area": "Flexibility"},
        {"workout": "Walking", "duration": "30 mins", "focus_area": "General Mobility"},
        {"workout": "Foam Rolling + Breathing", "duration": "25 mins", "focus_area": "Recovery"},
    ]

    if goal == "weight_loss":
        base_plan = weight_loss_plan
    elif goal == "muscle_gain":
        base_plan = muscle_gain_plan
    elif goal == "recovery":
        base_plan = recovery_plan
    else:
        base_plan = recovery_plan  # fallback

    full_plan = [base_plan[i % len(base_plan)] for i in range(days)]

    return {"plan": full_plan}
