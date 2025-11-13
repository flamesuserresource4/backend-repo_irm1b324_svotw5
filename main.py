import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Dict

app = FastAPI(title="StemLab Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prepare storage directories (safe no-op if not used)
try:
    BASE_DIR = os.getcwd()
    UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
    OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
except Exception:
    # In extremely restricted environments, ignore fs setup errors
    UPLOAD_DIR = "uploads"
    OUTPUT_DIR = "outputs"


@app.get("/")
def root():
    return {"message": "Audio Processing Backend Ready"}


@app.get("/api/hello")
def hello():
    return {"message": "Hello from the backend API!"}


@app.get("/test")
def test():
    return {
        "backend": "✅ Running",
        "note": "Audio processing temporarily disabled to ensure server startup.",
    }


@app.post("/api/process")
async def process_audio(_: UploadFile = File(...)) -> Dict:
    # Placeholder to guarantee boot; real DSP stack can be enabled once environment is ready
    raise HTTPException(status_code=501, detail="Audio processing not enabled in this environment. Choose 'Enable lightweight processing' and I'll switch to a compatible stack.")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
