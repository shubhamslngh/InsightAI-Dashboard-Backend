🧠 InsightAI Dashboard

InsightAI is an intelligent dashboard that generates, tracks, and visualizes actionable tasks from meeting transcripts using FastAPI, Next.js, and Gemini AI.
It allows teams to group tasks by projects, assign priorities, and monitor progress visually using charts.

🚀 Tech Stack
🖥️ Frontend

Next.js 16 (App Router + Turbopack)

React 19

Tailwind CSS v4

shadcn/ui components

Recharts for data visualization

⚙️ Backend

FastAPI (Python 3.9)

Uvicorn

Supabase (PostgreSQL) for data persistence

Pydantic v2

Gemini 1.5 Flash LLM (via google-generativeai)

🧩 Architecture Overview
📦 InsightAI
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── generate.py     → Gemini AI task extraction
│   │   │   └── tasks.py        → CRUD endpoints for tasks/projects
│   │   └── services/
│   │       └── llm_service.py  → Gemini API integration
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx            → Dashboard layout
│   │   ├── components/
│   │   │   ├── TranscriptForm.tsx
│   │   │   ├── TaskList.tsx
│   │   │   ├── ProgressPie.tsx
│   │   │   └── PriorityBar.tsx
│   └── package.json
│
└── README.md

🌐 Hosted App

🔗 Frontend: https://insight-ai-dashboard-frontend.vercel.app/

🔗 Backend API: https://insightai-backend.onrender.com

⚡ Features

✅ Generate AI-based action items from transcripts
✅ Group tasks by project name
✅ Edit, delete, and mark tasks as completed
✅ Color-coded priorities (High, Medium, Low)
✅ Interactive charts for progress and priority distribution
✅ Supabase-backed persistence layer

🧱 Setup Instructions
🖥️ Local Setup
1️⃣ Clone the Repositories
git clone https://github.com/shubhamslngh/InsightAI-Dashboard-Backend.git
git clone https://github.com/shubhamslngh/InsightAI-Dashboard-Frontend.git

🧩 Backend Setup (FastAPI)
2️⃣ Create and Activate Virtual Environment
cd InsightAI-Dashboard-Backend
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Create .env
GEMINI_API_KEY=your_gemini_api_key_here
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

5️⃣ Run Server
uvicorn app.main:app --reload


Backend runs on http://127.0.0.1:8000

🖥️ Frontend Setup (Next.js)
6️⃣ Install Dependencies
cd ../InsightAI-Dashboard-Frontend
npm install

7️⃣ Create .env.local
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000

8️⃣ Run Dev Server
npm run dev


Frontend runs on http://localhost:3000

🌍 Hosted Setup (Render/Supabase)

Push both repos to GitHub.

Create a Render Web Service for:

Frontend (Next.js → build npm run build, start npm start)

Backend (FastAPI → start uvicorn app.main:app)

Add environment variables on Render:

GEMINI_API_KEY

SUPABASE_URL

SUPABASE_KEY

📊 Dashboard Previews
Progress	Priority	Task List
🟢 Pie chart for completed vs pending	🟠 Bar chart grouped by priority	📝 Editable + color-coded
🧠 LLM Integration

The backend uses Gemini 1.5 Flash for transcript parsing:

Extracts action items and priorities from natural-language meeting notes.

Returns structured JSON for display in the dashboard.

🧩 Level Completed

✅ Level 2 – Full CRUD + Persistent Database + Charts + Gemini Integration

🧑‍💻 Author

Shubham Singh