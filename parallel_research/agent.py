"""
ParallelAgent — three researchers run concurrently, then a synthesizer.

google_search is a Gemini built-in grounding tool.
Rule: agents using google_search must have NO other tools.
Rule: each parallel branch must use a UNIQUE output_key.

Run: adk web  →  pick "parallel_research"
Ask: "Research the future of renewable energy"
"""
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

MODEL = "gemini-flash-latest"

renewable_researcher = LlmAgent(
    name="RenewableResearcher",
    model=MODEL,
    description="Researches renewable energy trends.",
    instruction=(
        "Research the 3 most important recent developments in renewable energy. "
        "Output a 2-sentence summary."
    ),
    tools=[google_search],
    output_key="renewable_result",
)

ev_researcher = LlmAgent(
    name="EVResearcher",
    model=MODEL,
    description="Researches electric vehicle technology trends.",
    instruction=(
        "Research the latest key advances in electric vehicle technology. "
        "Output a 2-sentence summary."
    ),
    tools=[google_search],
    output_key="ev_result",
)

carbon_researcher = LlmAgent(
    name="CarbonResearcher",
    model=MODEL,
    description="Researches carbon capture methods.",
    instruction=(
        "Research the most promising current carbon capture methods and breakthroughs. "
        "Output a 2-sentence summary."
    ),
    tools=[google_search],
    output_key="carbon_result",
)

research_team = ParallelAgent(
    name="ResearchTeam",
    description="Three concurrent researchers covering renewable energy, EVs, and carbon capture.",
    sub_agents=[renewable_researcher, ev_researcher, carbon_researcher],
)

synthesizer = LlmAgent(
    name="Synthesizer",
    model=MODEL,
    description="Combines parallel research into a structured report.",
    instruction=(
        "Combine the following research into one structured markdown report with three sections:\n\n"
        "**Renewable Energy:**\n{renewable_result}\n\n"
        "**Electric Vehicles:**\n{ev_result}\n\n"
        "**Carbon Capture:**\n{carbon_result}\n\n"
        "Add a short 'Key Takeaways' section at the end."
    ),
)

root_agent = SequentialAgent(
    name="ResearchAndSynthesize",
    description="Fan-out to three parallel researchers, then synthesize into one report.",
    sub_agents=[research_team, synthesizer],
)
