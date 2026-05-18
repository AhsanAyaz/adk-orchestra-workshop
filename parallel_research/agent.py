"""
STEP 3 — Parallel Research (Fan-Out / Gather)

Goal: three researchers run concurrently, each with a UNIQUE output_key.
A Synthesizer combines them after (wrapped in SequentialAgent).

Rules:
  - google_search is a Gemini grounding tool — no other tools allowed on the same agent.
  - Each parallel branch must write to a DIFFERENT output_key (else: silent overwrite).

To activate:
  1. Remove the `# ` prefix from every line in the block below the marker.
  2. Save. Run `adk web` and pick `parallel_research`.

Test prompt:
  "Research the future of renewable energy"
"""
from google.adk.agents import LlmAgent

# Placeholder — overridden once the real code below is uncommented.
root_agent = LlmAgent(
    name="parallel_research_NOT_BUILT",
    model="gemini-flash-latest",
    description="Placeholder. Uncomment the code in agent.py to activate.",
    instruction=(
        "Reply with exactly: "
        "'This agent is not built yet. Open parallel_research/agent.py "
        "and uncomment the code block to activate me.'"
    ),
)

# ════════════════ UNCOMMENT EVERYTHING BELOW THIS LINE ════════════════

# from google.adk.agents import ParallelAgent, SequentialAgent
# from google.adk.tools import google_search
#
# MODEL = "gemini-flash-latest"
#
# renewable_researcher = LlmAgent(
#     name="RenewableResearcher",
#     model=MODEL,
#     description="Researches renewable energy trends.",
#     instruction=(
#         "Research the 3 most important recent developments in renewable energy. "
#         "Output a 2-sentence summary."
#     ),
#     tools=[google_search],
#     output_key="renewable_result",
# )
#
# ev_researcher = LlmAgent(
#     name="EVResearcher",
#     model=MODEL,
#     description="Researches electric vehicle technology trends.",
#     instruction=(
#         "Research the latest key advances in electric vehicle technology. "
#         "Output a 2-sentence summary."
#     ),
#     tools=[google_search],
#     output_key="ev_result",
# )
#
# carbon_researcher = LlmAgent(
#     name="CarbonResearcher",
#     model=MODEL,
#     description="Researches carbon capture methods.",
#     instruction=(
#         "Research the most promising current carbon capture methods and breakthroughs. "
#         "Output a 2-sentence summary."
#     ),
#     tools=[google_search],
#     output_key="carbon_result",
# )
#
# research_team = ParallelAgent(
#     name="ResearchTeam",
#     description="Three concurrent researchers covering renewable energy, EVs, and carbon capture.",
#     sub_agents=[renewable_researcher, ev_researcher, carbon_researcher],
# )
#
# synthesizer = LlmAgent(
#     name="Synthesizer",
#     model=MODEL,
#     description="Combines parallel research into a structured report.",
#     instruction=(
#         "Combine the following research into one structured markdown report with three sections:\n\n"
#         "**Renewable Energy:**\n{renewable_result}\n\n"
#         "**Electric Vehicles:**\n{ev_result}\n\n"
#         "**Carbon Capture:**\n{carbon_result}\n\n"
#         "Add a short 'Key Takeaways' section at the end."
#     ),
# )
#
# root_agent = SequentialAgent(
#     name="ResearchAndSynthesize",
#     description="Fan-out to three parallel researchers, then synthesize into one report.",
#     sub_agents=[research_team, synthesizer],
# )
