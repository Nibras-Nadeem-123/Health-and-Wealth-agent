import chainlit as cl
from agent.planner_agent import planner_agent 
from agents import Runner, InputGuardrailTripwireTriggered, set_tracing_disabled
from openai.types.responses import ResponseTextDeltaEvent
from guardrails.input_guard import check_input_guardrails


set_tracing_disabled(True)  # Disable tracing for performance


# Shared memory across session
conversation_history = []
agent_state = {}
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
@cl.on_message
async def handle_user_message(message: cl.Message) -> None:
    user_input = message.content.strip()

    try:
        # Input safety check
        check_input_guardrails(user_input)

        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})

        # Send placeholder message
        response_msg = cl.Message(content="Thinking...")

        # Run planner agent with history + state
        result = Runner.run_streamed(starting_agent=planner_agent(), input=conversation_history)
        # await cl.Message(content=result.final_output).send()

        # # Stream each response token as it comes
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                await response_msg.stream_token(event.data.delta)

        # Optional: notify if a different agent handled the request
        if result.last_agent.name != planner_agent().name:
            await cl.Message(content=f"🤝 Handoff: {result.last_agent.name} responded.").send()

    except InputGuardrailTripwireTriggered as e:
        await cl.Message(content=f"⚠️ Input blocked by guardrails: {e}").send()
   
