"""
LoopAgent — writer ↔ critic, exits when critic calls exit_loop
or max_iterations is hit.

Run: adk web  →  pick "loop_refinement"
Ask: "Write a short blog post about why Python is great for beginners"
"""
from google.adk.agents import LlmAgent, LoopAgent
from google.adk.tools.tool_context import ToolContext

MODEL = "gemini-flash-latest"


def exit_loop(tool_context: ToolContext) -> dict:
    """Call this tool ONCE when the document is clear, complete, and publish-ready.
    Call it exactly one time and do not call it again.

    Returns:
        dict: Status confirmation. The loop will terminate after this call.
    """
    tool_context.actions.escalate = True
    return {"status": "loop_exited", "message": "Document approved. Loop terminated."}


writer = LlmAgent(
    name="Writer",
    model=MODEL,
    description="Writes and improves a document based on critic feedback.",
    instruction=(
        "You are a skilled writer. Your job is to produce or improve a document.\n\n"
        "Current document:\n{current_doc?}\n\n"
        "Critic feedback to address (empty on first pass):\n{critique?}\n\n"
        "If this is the first pass, write a complete first draft based on the user's original request.\n"
        "If there is critique, revise the document to address every point.\n"
        "Output ONLY the full revised document — no explanations, no commentary."
    ),
    output_key="current_doc",
)

critic = LlmAgent(
    name="Critic",
    model=MODEL,
    description="Reviews the document and either approves it or requests improvements.",
    instruction=(
        "You are an exacting editor. Review this document:\n\n"
        "{current_doc}\n\n"
        "Decide ONE of these two paths and do exactly one of them:\n\n"
        "PATH A — Document is clear, well-structured, engaging, error-free, and publish-ready:\n"
        "  1. Call the exit_loop tool exactly ONCE.\n"
        "  2. Then output the single word: Approved.\n"
        "  3. STOP. Do not call exit_loop again.\n\n"
        "PATH B — Document still needs work:\n"
        "  1. Do NOT call exit_loop.\n"
        "  2. Output exactly 2-3 specific, actionable improvements as a bullet list.\n"
        "  3. Nothing else."
    ),
    tools=[exit_loop],
    output_key="critique",
)

root_agent = LoopAgent(
    name="RefinementLoop",
    description="Iteratively refines a document with a Writer–Critic loop until publish-ready.",
    max_iterations=5,
    sub_agents=[writer, critic],
)
