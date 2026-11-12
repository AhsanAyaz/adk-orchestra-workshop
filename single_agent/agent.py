"""
STEP 1 — Single Agent (The Soloist)

Goal: one LlmAgent + one custom Python tool (weather lookup).

To activate:
  1. Read the commented code block below the marker.
  2. Remove the `# ` prefix from each of those lines.
     VS Code shortcut: select the block, press Cmd-/ (Mac) or Ctrl-/ (Win/Linux).
  3. Save. Then run `adk web` and pick `single_agent` from the dropdown.

Test prompt:
  "What's the weather in Stockholm?"
"""
from google.adk.agents import LlmAgent

# Placeholder — gets overridden once you uncomment the real code below.
root_agent = LlmAgent(
    name="single_agent_NOT_BUILT",
    model="gemini-flash-latest",
    description="Placeholder. Uncomment the code in agent.py to activate.",
    instruction=(
        "Reply with exactly: "
        "'This agent is not built yet. Open single_agent/agent.py and "
        "uncomment the code block to activate me.'"
    ),
)

# ════════════════ UNCOMMENT EVERYTHING BELOW THIS LINE ════════════════

# MODEL = "gemini-flash-latest"
#
#
# def get_weather(city: str) -> dict:
#     """Retrieves the current weather for a city.
#
#     Args:
#         city: The city name to look up.
#
#     Returns:
#         dict: status and result or error message.
#     """
#     data = {
#         "stockholm": "Sunny, 22°C",
#         "london": "Cloudy, 15°C",
#         "new york": "Partly cloudy, 18°C",
#         "tokyo": "Rainy, 20°C",
#         "prishtina": "Clear, 24°C",
#         "berlin": "Overcast, 17°C",
#         "paris": "Sunny, 21°C",
#     }
#     report = data.get(city.lower())
#     if report:
#         return {"status": "success", "report": report}
#     return {"status": "error", "error_message": f"No weather data for '{city}'."}
#
#
# root_agent = LlmAgent(
#     name="SingleAgent",
#     model=MODEL,
#     description="A weather assistant that looks up current conditions for cities.",
#     instruction=(
#         "You help users check the weather. "
#         "Always use the get_weather tool to look up conditions for any city they ask about."
#     ),
#     tools=[get_weather],
# )
