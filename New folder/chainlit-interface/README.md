# Chainlit Interface Project

This project implements a user interface using Chainlit for running various agents, including a maths agent, physics agent, and triage agent.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd chainlit-interface
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory and add any necessary environment variables.

4. **Run the application:**
   Execute the following command to start the Chainlit interface:
   ```bash
   chainlit run src/main.py
   ```

## Usage Guidelines

- Follow the instructions in `src/chainlit.md` for detailed usage of the Chainlit interface.
- Ensure that all agents are properly defined in `src/agents/all_agents.py`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.