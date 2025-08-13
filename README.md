## enigma-mcp-examples

Minimal examples showing how to use Enigma's MCP tools from an OpenAI Agent (via the `openai-agents` Python SDK).

Refer to the Enigma MCP Server documentation at https://ai.enigma.com for more details about tools supported, expected results and alternative configurations.

### What’s here
- `examples/openai-agents/single_agent.py`: A simple agent that connects to an MCP server over HTTP and streams a response to a business onboarding question.
- `examples/openai-agents/requirements.txt`: Python dependencies for the example.

### Prerequisites
- Python 3.10+ recommended
- An OpenAI API key (`OPENAI_API_KEY`)
- Access to an Enigma MCP server endpoint and API key (`MCP_SERVER_URL`, `MCP_API_KEY`)

### Quick start
1) Create and activate a virtual environment

```bash
python3 -m venv .venv && source .venv/bin/activate
```

2) Install dependencies

```bash
pip install -r examples/openai-agents/requirements.txt
```

3) Configure environment

Create a `.env` file in the project root (the script uses `python-dotenv` to load it when run from the root):

```bash
OPENAI_API_KEY=your-openai-key
MCP_SERVER_URL=https://mcp.enigma.com/http-key
MCP_API_KEY=your-enigma-api-key
```

4) Run the example

```bash
python examples/openai-agents/single_agent.py
```

You’ll see the agent stream its reasoning/output to the console.

### How it works
`examples/openai-agents/single_agent.py`:
- Initializes an `Agent` with instructions to analyze a business.
- Connects to the MCP server over HTTP using `MCPServerStreamableHttp` with `MCP_SERVER_URL` and `MCP_API_KEY`.
- Sends a sample message: “Should I onboard this business? Origin Coffee in Saranac Lake, NY”.
- Streams and prints the model’s output as it arrives.


### License
MIT or project’s root license, if applicable.