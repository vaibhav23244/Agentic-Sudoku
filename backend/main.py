from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from agents import generate_sudoku_puzzle, solve_sudoko_puzzle
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000/",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SudokuPuzzle(BaseModel):
    puzzle: List[List[int]]

@app.get("/generate_puzzle", response_model=SudokuPuzzle)
def generate_sudoku_route():
    puzzle = generate_sudoku_puzzle()
    puzzle_data = {"puzzle": puzzle.content.puzzle}  
    return puzzle_data

@app.post("/solve_puzzle", response_model=SudokuPuzzle)
def solve_sudoku_route(puzzle: List[List[int]]):
    solved_puzzle = solve_sudoko_puzzle(puzzle)
    puzzle_data = {"puzzle": solved_puzzle.content.puzzle}  
    return puzzle_data