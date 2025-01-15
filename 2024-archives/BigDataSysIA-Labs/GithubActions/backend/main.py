from pydantic import BaseModel
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()


# Request model
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_with_openai(request: ChatRequest):
    try:
        response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Be concise and clear. Reply in a single word."},
                    {"role": "user", "content": request.message}
                ],
                max_tokens=64
            )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {str(e)}")

# Simple GET endpoint for testing
@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

# Simple POST endpoint for testing
class TestPostRequest(BaseModel):
    name: str

@app.post("/test")
def test_post(request: TestPostRequest):
    return {"greeting": f"Hello, {request.name}!"}
