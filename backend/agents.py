from os import getenv
from typing import List
from textwrap import dedent
from agno.agent import Agent
from pydantic import BaseModel
from dotenv import load_dotenv
from agno.models.groq import Groq

load_dotenv(override=True)

class SudokuResponse(BaseModel):
    puzzle: List[List[int]]

def generate_sudoku_puzzle():
    sudoko_generator = Agent(
    name="Sudoku Generator",
    model=Groq(id="gemma2-9b-it", api_key=getenv("GROQ_API_KEY")),
    response_model=SudokuResponse,
    description=dedent("""\
        You are a Sudoku puzzle generator agent. Your task is to generate a valid and solvable 9x9 Sudoku puzzle with a **different layout** every time.
        
        Ensure that each puzzle is distinct from the last, with a random clue distribution. 
        Each puzzle should be randomly generated, avoiding repetition of previous puzzles.

        SUDOKU RULES:
        - The board is a 9x9 grid divided into 9 smaller 3x3 boxes.
        - Each row, column, and 3x3 box must contain the numbers 1 through 9 with no repetition.
        - The puzzle must have a unique solution.

        PUZZLE REQUIREMENTS:
        - Generate a **random** puzzle with **a different layout** each time.
        - Ensure the puzzle is solvable by logical methods.
        - Avoid puzzles that are too easy or too difficult by balancing the clue distribution.

        RESPONSE FORMAT:
        - Provide a 9x9 grid as a 2D array of integers.
        - Use 0 to represent empty cells.
        - Example format:
        [
            [0, 2, 0, 0, 8, 0, 0, 7, 0],
            [4, 7, 0, 0, 0, 9, 0, 0, 0],
            ...
            [6, 0, 0, 0, 9, 0, 0, 5, 3]
        ]

        ADDITIONAL TIPS:
        - Ensure that the puzzle adheres strictly to Sudoku rules.
        - Do not solve the puzzle or provide solutions in the response.
        - Only respond with the 2D array and no extra text.
        """),
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
    )
    sudoko_puzzle = sudoko_generator.run("Generate a valid and solvable 9x9 Sudoku puzzle.")
    return sudoko_puzzle

def solve_sudoko_puzzle(puzzle: List[List[int]]) -> SudokuResponse:
    sudoku_solver = Agent(
        name="Sudoku Solver",
        model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct", api_key=getenv("GROQ_API_KEY")),
        response_model=SudokuResponse,
        description=dedent("""\
            You are a Sudoku solver. Your task is to solve a 9x9 Sudoku puzzle.

            SUDOKU RULES:
            - Each row, column, and 3x3 box must contain the numbers 1 through 9 with no repetition.
            - The board is valid and has a unique solution.

            RESPONSE FORMAT:
            - Provide the solved 9x9 Sudoku puzzle as a 2D list of integers.
            - Example format:
            [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                ...
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
            ]

            INSTRUCTIONS:
            - Only respond with the 2D list.
            - Do not include explanation or extra text.
        """),
        markdown=True,
        debug_mode=True,
        show_tool_calls=True,
    )

    prompt = f"Solve this Sudoku puzzle:\n{puzzle}"
    solved = sudoku_solver.run(prompt)
    return solved