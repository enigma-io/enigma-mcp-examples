import asyncio
import os
from agents import Agent, Runner
from agents.mcp import MCPServer, MCPServerStreamableHttp
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv

load_dotenv()   

async def run(mcp_server: MCPServer):
    agent = Agent(
        name="Enigma Onboarding Agent",
        instructions="Use the tools to analyze the business",
        mcp_servers=[mcp_server],
    )

    message = "Should I onboard this business? Origin Coffee in Saranac Lake, NY"
    print(f"Running: {message}")

    result =  Runner.run_streamed(starting_agent=agent, input=message)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


async def main():
    async with MCPServerStreamableHttp(
        client_session_timeout_seconds=30,
        name="Enigma Business Intelligence Tools",
        cache_tools_list=True,
        params={
            "url": os.getenv("MCP_SERVER_URL"),
            "headers": {"x-api-key": os.getenv("MCP_API_KEY")},
        },
    ) as server:
        await server.connect()
        await run(server)


if __name__ == "__main__":
    asyncio.run(main())