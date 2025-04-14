# 🧩 Agentic Sudoku — AI-Powered Sudoku Generator & Solver

Real-time, full-stack Sudoku web app powered by Large Language Models (LLMs), multi-agent orchestration via **Agno**, and ultra-fast inference through **Groq**. Generate unique puzzles and solve them live — all with structured, logic-enforced AI.
---

## 📂 Project Structure

```bash
.
├── frontend/   # Next.js + TailwindCSS based client app
└── backend/    # FastAPI server with multi-agent LLM logic
⚙️ Tech Stack
🖥 Frontend
Next.js (App Router)

TailwindCSS

Axios for API communication

Shadcn/UI (optional UI enhancements)

🧠 Backend
FastAPI (Python)

Agno Framework for agent orchestration

Pydantic for response schema validation

Groq API for low-latency LLM inference

Open Source LLMs: Google Gemma 2, Meta LLaMA 4

🧠 Agents Description
Agent	Task Description
🎲 Generator	Produces a valid, logic-compliant 9x9 Sudoku puzzle
🧩 Solver	Solves the puzzle step-by-step with strict adherence to Sudoku rules
Each agent operates independently and is defined declaratively using Agno's @agent decorator.

🚀 How to Run Locally
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/vaibhav23244/Agentic-Sudoku.git
cd Agentic-Sudoku
2. Backend Setup
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
🔐 Make sure to add your Groq API key to the .env file:

env
Copy
Edit
GROQ_API_KEY=your_key_here
3. Frontend Setup
bash
Copy
Edit
cd frontend
npm install
npm run dev
Open http://localhost:3000 to view the app in your browser.


📚 Why This Matters
“LLMs aren’t just for text — they can reason, solve logic problems, and teach.”

This project explores how structured LLM reasoning can be used in:

Games & Brain Trainers

Educational Tools

Agentic AI UX Design

Interview/Skill Assessment

🛠️ Future Plans
 Add step-by-step visual solving

 Integrate chat-based explanation agent

 Deploy live on Vercel + Railway

 Add mobile responsiveness

🤝 Acknowledgements
Powered by @Groq 🚀

Multi-agent orchestration via @Agno

Models: LLaMA 4, Gemma 2

UI inspired by logic game design aesthetics

📬 Contact
Have ideas, feedback, or just want to connect?

Vaibhav
🔗 LinkedIn: https://www.linkedin.com/in/vaibhaav-varma-8b4382154/
💌 vaibhav23244@gmail.com

