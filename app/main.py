from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import generate, tasks, projects

app = FastAPI(title="AI Action Items API")

# Allow frontend calls (Next.js/React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate.router)
app.include_router(tasks.router)
app.include_router(projects.router)

@app.get("/")
def root():
    return {"message": "AI Action Items API is running"}
