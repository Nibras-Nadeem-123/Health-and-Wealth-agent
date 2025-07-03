from agents import InputGuardrailTripwireTriggered

BLOCKED_PHRASES = [
    "extreme weight loss",
    "starve",
    "stop eating",
    "lose 10kg in 1 week",
    "fastest way to lose"
]

def check_input_guardrails(user_input: str):
    """Raise a tripwire if unsafe or banned input is detected."""
    for phrase in BLOCKED_PHRASES:
        if phrase in user_input.lower():
            raise InputGuardrailTripwireTriggered(
                f"Input contains an unsafe or banned health query: '{phrase}'"
            )           
