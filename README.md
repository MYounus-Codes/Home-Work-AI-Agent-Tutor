# Homework Tutor

Homework Tutor is an AI-powered assistant designed to help students with Math and Physics problems. It provides step-by-step explanations, curated resources, and motivational support, all in a friendly chat interface. Powered by advanced language models and real-time educational search, Homework Tutor makes learning interactive and effective.

---

## Features

- **Maths Tutor:**
  Get clear, step-by-step solutions for math problems, including definitions, logical steps, and final answers. Uses LaTeX for mathematical notation and provides curated resources and motivational quotes.

- **Physics Tutor:**
  Receive detailed explanations for physics concepts and problems, including formulas, solution steps, and references to trusted sites and videos.

- **Academic Triage Agent:**
  Automatically detects whether your question is about math or physics and routes it to the correct tutor. Ensures you get the most relevant help.

- **Resource Integration:**
  Uses a custom educational search tool to find up-to-date tutorials, documentation, videos, and PDFs from trusted educational sites.

- **Friendly Greeter:**
  Welcomes users and responds warmly to greetings, making the experience more engaging.

---

## How It Works

1. **Start a Chat:**
   The assistant greets you and asks what you want to learn.

2. **Ask a Question:**
   Type your math or physics question. The triage agent analyzes your query and sends it to the appropriate tutor.

3. **Get Step-by-Step Help:**
   The tutor provides a structured, easy-to-follow solution, including explanations, resources, and practice problems.

4. **Access Resources:**
   Receive links to tutorials, documentation, videos, and PDFs relevant to your question.

---

## Technologies Used

- Python 3.10+
- Chainlit (for chat interface)
- Google Custom Search API (for educational resource search)
- Gemini Language Model (for AI responses)
- dotenv (for environment variable management)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/homework-tutor.git
cd homework-tutor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root and add your API keys:

```
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_SEARCHING_API_KEY=your_google_search_api_key
GOOGLE_CSE_ID=your_google_cse_id
```

### 4. Run the App

```bash
python app.py
```

---

## Usage

- Open the app in your browser (if using Chainlit, it will provide a local URL).
- Start chatting!  
  Example questions:
  - "How do I solve quadratic equations?"
  - "Explain Newton's second law."
  - "Show me a video tutorial on integration."
  - "What is the formula for kinetic energy?"

---

## Deployment

You can deploy Homework Tutor for free using platforms like [Render](https://render.com/), [Railway](https://railway.app/), or [Deta Space](https://deta.space/).

**Render Example:**
1. Push your code to GitHub.
2. Create a `requirements.txt` and `Procfile` (`web: python app.py`).
3. Connect your repo on Render, set environment variables, and deploy.

---

## File Structure

```
homework-tutor/
│
├── app.py                  # Main application file (Chainlit chat logic)
├── all_agents.py           # Agent definitions and instructions
├── web_searching_tool.py   # Educational search tool
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
└── README.md               # This file
```

---

## Customization

- **Add More Subjects:**  
  Extend `all_agents.py` with new agents for Chemistry, Biology, etc.

- **Improve Search:**  
  Add more educational sites in `web_searching_tool.py` for broader resource coverage.

- **Change Model:**  
  Swap out the Gemini model for another supported LLM if desired.

---

## Troubleshooting

- **API Key Errors:**  
  Make sure your `.env` file is correctly set up and keys are valid.

- **Search Not Working:**  
  Check your Google Custom Search Engine configuration and API quota.

- **App Not Starting:**  
  Ensure all dependencies are installed and you’re using a compatible Python version.

---

## Contributing

Pull requests and suggestions are welcome!  
Please open an issue for bugs or feature requests.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [Chainlit](https://chainlit.io/)
- [Google Custom Search](https://developers.google.com/custom-search/v1/overview)
- [Gemini Language Model](https://ai.google.dev/)
- Educational sites: Khan Academy, Brilliant, Mathway, Physics Classroom, YouTube

---

## Contact

For questions or support, open an issue or email [your-email@example.com](mailto:your-email@example.com).

---

**Happy Learning! 🚀**
