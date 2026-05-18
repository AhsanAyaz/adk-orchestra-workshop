"""
STEP 6 — Content Orchestra (Full Composition)

The full pipeline: research → outline → draft → iterative refinement.

Architecture:
  SequentialAgent (root)
  ├── 1. ResearchTeam       (SequentialAgent — trends, audience, competitors)
  ├── 2. Outliner           (reads research → outline)
  ├── 3. Drafter            (reads outline → first draft)
  └── 4. RefinementLoop     (LoopAgent — Reviser ↔ Critic, max 3 passes)

To activate:
  1. Remove the `# ` prefix from every line in the block below the marker.
  2. Save. Run `adk web` and pick `content_orchestra`.

Test prompt:
  "AI developer tools in 2026"
"""
from google.adk.agents import LlmAgent

# Placeholder — overridden once the real code below is uncommented.
root_agent = LlmAgent(
    name="content_orchestra_NOT_BUILT",
    model="gemini-flash-latest",
    description="Placeholder. Uncomment the code in agent.py to activate.",
    instruction=(
        "Reply with exactly: "
        "'This agent is not built yet. Open content_orchestra/agent.py "
        "and uncomment the code block to activate me.'"
    ),
)

# ════════════════ UNCOMMENT EVERYTHING BELOW THIS LINE ════════════════

# from google.adk.agents import LoopAgent, SequentialAgent
# from google.adk.tools import google_search
# from google.adk.tools.tool_context import ToolContext
#
# MODEL = "gemini-flash-latest"
#
# # ── Stage 1: Sequential Research ──────────────────────────────────────────
#
# trend_researcher = LlmAgent(
#     name="TrendResearcher",
#     model=MODEL,
#     description="Finds current trends for a given topic.",
#     instruction=(
#         "Find 3 current trends about: {topic?}\n"
#         "If no topic is provided, use the user's original message as the topic.\n"
#         "Output a short bullet list of trends."
#     ),
#     tools=[google_search],
#     output_key="trends",
# )
#
# audience_researcher = LlmAgent(
#     name="AudienceResearcher",
#     model=MODEL,
#     description="Identifies the target audience for a topic.",
#     instruction=(
#         "Identify the target audience for: {topic?}\n"
#         "If no topic is provided, use the user's original message as the topic.\n"
#         "Output 3 concise persona bullets (role, goal, pain point)."
#     ),
#     tools=[google_search],
#     output_key="audience",
# )
#
# competitor_researcher = LlmAgent(
#     name="CompetitorResearcher",
#     model=MODEL,
#     description="Finds competing content for a topic.",
#     instruction=(
#         "Find 3 existing articles or resources about: {topic?}\n"
#         "If no topic is provided, use the user's original message as the topic.\n"
#         "Output: title + one-line summary for each."
#     ),
#     tools=[google_search],
#     output_key="competitors",
# )
#
# research_team = SequentialAgent(
#     name="ResearchTeam",
#     description="Three sequential researchers: trends, audience, and competitors.",
#     sub_agents=[trend_researcher, audience_researcher, competitor_researcher],
# )
#
# # ── Stage 2: Outline ──────────────────────────────────────────────────────
#
# outliner = LlmAgent(
#     name="Outliner",
#     model=MODEL,
#     description="Builds a content outline from research.",
#     instruction=(
#         "Build a 5-section article outline for: {topic?}\n\n"
#         "Use this research:\n"
#         "Trends: {trends}\n"
#         "Audience: {audience}\n"
#         "Competitors (to differentiate from): {competitors}\n\n"
#         "Output a numbered outline with a one-sentence description per section."
#     ),
#     output_key="outline",
# )
#
# # ── Stage 3: First Draft ──────────────────────────────────────────────────
#
# drafter = LlmAgent(
#     name="Drafter",
#     model=MODEL,
#     description="Writes a first draft from the outline.",
#     instruction=(
#         "Write a complete first draft article following this outline:\n{outline}\n\n"
#         "Target audience: {audience}\n"
#         "Make it engaging, clear, and approximately 400 words."
#     ),
#     output_key="draft",
# )
#
# # ── Stage 4: Refinement Loop ──────────────────────────────────────────────
#
# def exit_loop(tool_context: ToolContext) -> dict:
#     """Call ONLY when the draft is clear, accurate, well-structured, and publish-ready."""
#     tool_context.actions.escalate = True
#     return {}
#
#
# reviser = LlmAgent(
#     name="Reviser",
#     model=MODEL,
#     description="Revises the draft based on critic feedback.",
#     instruction=(
#         "Revise the following article draft:\n{draft}\n\n"
#         "Apply this critique (empty on first revision pass):\n{critique?}\n\n"
#         "Output ONLY the full revised article."
#     ),
#     output_key="draft",  # intentionally overwrites draft each iteration
# )
#
# critic = LlmAgent(
#     name="Critic",
#     model=MODEL,
#     description="Reviews the draft and either approves or requests improvements.",
#     instruction=(
#         "Critique the following article:\n{draft}\n\n"
#         "Check: Is it clear, accurate, engaging, and well-structured for this audience?\n"
#         "Audience: {audience}\n\n"
#         "If the article is publish-ready, call exit_loop.\n"
#         "Otherwise, output exactly 2-3 specific improvements — nothing else."
#     ),
#     tools=[exit_loop],
#     output_key="critique",
# )
#
# refinement_loop = LoopAgent(
#     name="RefinementLoop",
#     description="Iterative revise–critique loop, max 3 passes.",
#     max_iterations=3,
#     sub_agents=[reviser, critic],
# )
#
# # ── Root: Full Orchestra ──────────────────────────────────────────────────
#
# root_agent = SequentialAgent(
#     name="ContentOrchestra",
#     description=(
#         "Full content pipeline: research → outline → draft → iterative refinement. "
#         "Give it a topic and it produces a polished article."
#     ),
#     sub_agents=[research_team, outliner, drafter, refinement_loop],
# )
