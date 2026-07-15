from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Human Behavior Intelligence Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Enable CORS (so your frontend can call this backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- ROOT ENDPOINT ----------
@app.get("/")
def root():
    return {"message": "Welcome to Human Behavior Intelligence Platform"}

# ---------- HEALTH CHECK ----------
@app.get("/health")
def health():
    return {"status": "ok"}

# ---------- AUTH ROUTES ----------
@app.post("/api/v1/auth/register")
def register(email: str, password: str, full_name: str):
    return {"message": f"User {email} registered successfully!"}

@app.post("/api/v1/auth/login")
def login(username: str, password: str):
    return {"access_token": "fake-token-12345", "token_type": "bearer"}

# ---------- PREDICTION ROUTE (Simple Version) ----------
@app.post("/api/v1/predict/single")
def predict(data: dict):
    text = data.get("text", "")
    if "love" in text.lower() or "happy" in text.lower():
        sentiment = "POSITIVE"
    elif "hate" in text.lower() or "sad" in text.lower():
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"
    return {"text": text, "results": {"sentiment": {"label": sentiment, "score": 0.95}}}
