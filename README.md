# ADK Orchestra — A Beginner's Workshop

A hands-on, ~60-minute workshop for building AI agents with **Google ADK**.

Open `index.html` in your browser for the full guided walkthrough. This README is just the quick-start.

---

## Quick start

```bash
# 1. Run setup (installs venv, deps, and optionally Gemini CLI)
./setup.sh

# 2. Add your free API key to .env
#    Get one at: https://aistudio.google.com/apikey

# 3. Activate the venv
source .venv/bin/activate

# 4. Launch the ADK playground
adk web
```

Then open `index.html` in your browser and follow along.

---

## What you'll build

| # | Agent                 | Concept                                     |
|---|----------------------|---------------------------------------------|
| 1 | `single_agent`        | One agent + one custom Python tool          |
| 2 | `sequential_pipeline` | Three agents chained — write → review → refactor |
| 3 | `parallel_research`   | Fan-out: three researchers + a synthesizer  |
| 4 | `loop_refinement`     | Writer ↔ Critic loop until publish-ready    |
| 5 | `mcp_travel`          | External MCP server (Airbnb search)         |
| 6 | `content_orchestra`   | Full composition of all primitives          |

---

## What's in the box

```
adk-orchestra-workshop/
├── index.html              # The workshop — open in browser
├── setup.sh                # One-shot installer
├── requirements.txt        # Python deps (google-adk, python-dotenv)
├── .env.example            # Template for your API key
├── single_agent/           # Agent 1
├── sequential_pipeline/    # Agent 2
├── parallel_research/      # Agent 3
├── loop_refinement/        # Agent 4
└── content_orchestra/      # Agent 6 (full pipeline)
```

Agent 5 (`mcp_travel/`) is built **by you** during the workshop — that's the MCP hands-on exercise.

---

## Requirements

- **Python 3.10+**
- **Node.js / npm** (for the MCP exercise and Gemini CLI bonus step)
- A free **Google AI Studio API key** — no credit card needed

---

## Tools used

- [Google ADK](https://google.github.io/adk-docs) — agent framework
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — optional, for the vibe-coding bonus step
- [Model Context Protocol](https://modelcontextprotocol.io) — external tool integration
