import chainlit as cl
from agents import Runner
from all_agents import triage_agent

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message(
        content="👋 Hello! I'm your homework tutor. I can help you with Math and Physics problems. What would you like to learn?"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    
    # Load history
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": message.content})

    context = {"history": history}

    # Detect if the query is likely to use the search tool
    uses_search_keywords = any(word in message.content.lower() for word in [
        "video", "link", "resource", "explain", "pdf", "youtube", "search", "tutorial", "documentation"
    ])
    step_label = "🔎 Searching..." if uses_search_keywords else "Thinking..."

    async with cl.Step(step_label):
        result = await Runner.run(
            triage_agent,
            input=message.content,
            context=context,
            max_turns=10,
        )

    reply = result.final_output
    await cl.Message(content=reply).send()

    # Update history
    history.append({"role": "assistant", "content": reply})
    cl.user_session.set("history", history)

    # Send documentation links
    if hasattr(result, "documentation_links") and result.documentation_links:
        doc_links = "\n".join(f"- {link}" for link in result.documentation_links)
        await cl.Message(content=f"📚 **Documentation Links:**\n{doc_links}").send()

    # Send YouTube/tutorial links
    if hasattr(result, "youtube_tutorials") and result.youtube_tutorials:
        yt_links = "\n".join(f"- {link}" for link in result.youtube_tutorials)
        await cl.Message(content=f"🎥 **Video Tutorials:**\n{yt_links}").send()

    # Send PDF links if available
    if hasattr(result, "pdf_links") and result.pdf_links:
        pdf_links = "\n".join(f"- {link}" for link in result.pdf_links)
        await cl.Message(content=f"📄 **PDF Resources:**\n{pdf_links}").send()
