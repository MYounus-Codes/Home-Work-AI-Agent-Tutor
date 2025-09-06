from agents import Runner
from all_agents import maths_agent, physics_agent, triage_agent
import asyncio

async def main():

    response = await Runner.run(
        triage_agent,
        input="Drive this equation: (a+b)² = a² + 2ab + b²",
    )

    print(response.final_output)


if __name__ == "__main__":
    asyncio.run(main())
