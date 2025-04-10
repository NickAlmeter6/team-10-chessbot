from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from evaluator import evaluate_move

app = FastAPI()

origins = [
    "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class MoveInput(BaseModel):
    fen: str  # board position in FEN
    move: str  # e.g., "e2e4"

@app.post("/evaluate")
def evaluate(input: MoveInput):
    bot_response = evaluate_move(input.fen, input.move)
    print("Hooray")
    #return {2}
    return {"bot_move": bot_response}
