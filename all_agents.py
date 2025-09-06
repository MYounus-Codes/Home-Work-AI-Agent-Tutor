from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from web_searching_tool import educational_search
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini/gemini-2.0-flash"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# === Maths Tutor ===
maths_agent = Agent(
    name="Maths-Tutor",
    instructions="""
**🧠 Step-by-Step Maths Tutor**
1. **Concept & Definition**: Use LaTeX for clarity.  
2. **Logical Steps**: Numbered, with **bold** key terms.  
3. **✅ Final Answer**  
4. **Resources**:  
   – Websites : Name + URL  
   – 🎥 1–2 current YouTube tutorials  
5. **Tone**: Supportive + motivational quote at end.

""",
    model=LitellmModel(model=MODEL),
    handoff_description="Expert Maths Tutor for step-by-step problem solving.",
    tools=[educational_search],
)

# === Physics Tutor ===
physics_agent = Agent(
    name="Physics-Tutor",
    instructions="""
**⚛️ Step-by-Step Physics Tutor**
1. **Concept & Formula**: Use LaTeX.  
2. **Solution Steps**: Clean, numbered, **bold** key ideas.  
3. **✅ Final Result**  
4. **References**:  
   – Trusted sites : Name + URL  
   – 🎥 1–2 recent YouTube videos  
5. **Tone**: Encouraging + brief motivational message.
""",
    model=LitellmModel(model=MODEL),
    handoff_description="Expert Physics Tutor for step-by-step explanations.",
    tools=[educational_search],
)

# === Greeting Agent ===
greeting_agent = Agent(
    name="Greeting-Agent",
    instructions="""
**👋 Friendly Greeter**
1. If user says “hi/bye/thanks”, reply warmly with emojis.  
2. Keep it short (<2 sentences).  
3. E.g.: “Hi there! 👋 How can I help today?”
""",
    model=LitellmModel(model=MODEL),
    handoff_description="Handles basic greetings and polite responses."
)


# === Triage Agent ===
triage_agent = Agent(
    name="Triage-Agent",
    instructions="""
**🔁 Academic Triage Bot**
1. Detect subject: math vs physics.  
2. Use educational_search(subject, query, 5).  
3. Route to correct tutor.  
4. Reply: “Let me pass this to [Maths‑Tutor/Physics‑Tutor].”  
5. Stay friendly and concise.
""",
    model=LitellmModel(model=MODEL),
    tools=[educational_search],
    handoffs=[maths_agent, physics_agent, greeting_agent],
)
