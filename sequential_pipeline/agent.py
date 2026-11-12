"""
STEP 2 — Sequential Pipeline (Assembly Line)

Goal: three agents chained — CodeWriter → CodeReviewer → CodeRefactorer.
Each step reads the previous step's output via session state.

To activate:
  1. Remove the `# ` prefix from every line in the block below the marker.
  2. Save. Run `adk web` and pick `sequential_pipeline`.

Test prompt:
  "Write a function that checks if a number is prime"

Watch the State tab — generated_code → review_comments → refactored_code
fill in one by one.
"""
from google.adk.agents import LlmAgent

# Placeholder — overridden once the real code below is uncommented.
root_agent = LlmAgent(
    name="sequential_pipeline_NOT_BUILT",
    model="gemini-flash-latest",
    description="Placeholder. Uncomment the code in agent.py to activate.",
    instruction=(
        "Reply with exactly: "
        "'This agent is not built yet. Open sequential_pipeline/agent.py "
        "and uncomment the code block to activate me.'"
    ),
)

# ════════════════ UNCOMMENT EVERYTHING BELOW THIS LINE ════════════════

# from google.adk.agents import SequentialAgent
#
# MODEL = "gemini-flash-latest"
#
# writer = LlmAgent(
#     name="CodeWriter",
#     model=MODEL,
#     description="Writes Python code from a user spec.",
#     instruction=(
#         "Write a clean Python implementation for the user's spec. "
#         "Output ONLY the code inside a ```python``` block. No explanations."
#     ),
#     output_key="generated_code",
# )
#
# reviewer = LlmAgent(
#     name="CodeReviewer",
#     model=MODEL,
#     description="Reviews generated code for bugs and quality issues.",
#     instruction=(
#         "Review the following Python code:\n"
#         "```python\n{generated_code}\n```\n\n"
#         "List any bugs, edge cases, or quality issues as a bullet list. "
#         "If the code looks good, say exactly: 'No major issues found.'"
#     ),
#     output_key="review_comments",
# )
#
# refactorer = LlmAgent(
#     name="CodeRefactorer",
#     model=MODEL,
#     description="Refactors code applying reviewer feedback.",
#     instruction=(
#         "Refactor the following Python code:\n"
#         "```python\n{generated_code}\n```\n\n"
#         "Apply these review comments:\n{review_comments}\n\n"
#         "Output ONLY the final improved code inside a ```python``` block."
#     ),
#     output_key="refactored_code",
# )
#
# root_agent = SequentialAgent(
#     name="CodePipeline",
#     description="A three-stage code pipeline: write → review → refactor.",
#     sub_agents=[writer, reviewer, refactorer],
# )
