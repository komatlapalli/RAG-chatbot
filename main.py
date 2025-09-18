from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "RAG chatbot backend is running"}