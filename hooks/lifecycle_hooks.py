
async def on_tool_start(event):
    print(f"[TOOL START] {event.tool_name} | Input: {event.input}")

async def on_tool_end(event):
    print(f"[TOOL END] {event.tool_name} | Output: {event.output}")

async def on_handoff(event):
    print(f"[HANDOFF] From: {event.from_agent} → To: {event.to_agent}")

async def on_error(agent_name: str, error: Exception):
    print(f"[ERROR] Agent: {agent_name} | Error: {str(error)}")
