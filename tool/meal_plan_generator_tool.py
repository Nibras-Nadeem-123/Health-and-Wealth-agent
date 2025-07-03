from agents import function_tool
from typing import TypedDict, List, Dict

class MealPlanInput(TypedDict):
    diet_preference: str  # e.g., vegetarian, keto, no_pref
    duration_days: int  # e.g., 5 or 7

class DayMealPlan(TypedDict):
    breakfast: str
    lunch: str
    dinner: str

class MealPlanOutput(TypedDict):
    plan: List[DayMealPlan]

@function_tool()
def meal_plan_generator_tool(input: MealPlanInput) -> MealPlanOutput:
    """Generates a personalized meal plan based on diet and duration."""

    diet = input["diet_preference"]
    days = input["duration_days"]

    vegetarian_meals = [
        {"breakfast": "Oatmeal with banana and chia seeds",
         "lunch": "Chickpea salad with hummus",
         "dinner": "Lentil curry with brown rice"},
        {"breakfast": "Greek yogurt with berries",
         "lunch": "Grilled tofu wrap",
         "dinner": "Vegetarian stir fry with quinoa"},
        {"breakfast": "Avocado toast with tomatoes",
         "lunch": "Paneer tikka with roti",
         "dinner": "Zucchini pasta with marinara sauce"},
    ]

    keto_meals = [
        {"breakfast": "Scrambled eggs with spinach",
         "lunch": "Grilled chicken salad with olive oil",
         "dinner": "Salmon with steamed broccoli"},
        {"breakfast": "Almond flour pancakes with cream",
         "lunch": "Zucchini noodles with pesto",
         "dinner": "Beef stir fry with cabbage"},
        {"breakfast": "Chia pudding with coconut milk",
         "lunch": "Tuna lettuce wraps",
         "dinner": "Grilled shrimp with cauliflower mash"},
    ]

    default_meals = [
        {"breakfast": "Boiled eggs and toast",
         "lunch": "Grilled chicken sandwich",
         "dinner": "Rice and mixed vegetables"},
        {"breakfast": "Smoothie with banana, spinach, and protein",
         "lunch": "Turkey wrap with salad",
         "dinner": "Pasta with tomato sauce and mushrooms"},
        {"breakfast": "Cereal with milk and fruit",
         "lunch": "Baked potato with beans",
         "dinner": "Grilled fish with green beans"},
    ]

    if diet == "vegetarian":
        base = vegetarian_meals
    elif diet == "keto":
        base = keto_meals
    else:
        base = default_meals

    full_plan = []
    for i in range(days):
        full_plan.append(base[i % len(base)])

    for day in full_plan:
        assert "breakfast" in day and "lunch" in day and "dinner" in day, \
            "Meal plan day is missing fields"

    return {"plan": full_plan}
