"use client";
import axios from "axios";
import { useState } from "react";
import { FaPlay } from "react-icons/fa";
import { BsStars } from "react-icons/bs";
import { FaGamepad } from "react-icons/fa";

const SudokuBoard = () => {
  const [isSolving, setIsSolving] = useState(false);
  const [isSolved, setIsSolved] = useState(false);
  const [isGenerating, setIsGenerating] = useState(false);
  const [board, setBoard] = useState<number[][]>([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
  ]);

  async function getNewPuzzle() {
    setIsGenerating(true);
    try {
      const response = await axios.get("http://127.0.0.1:8000/generate_puzzle");
      setBoard(response.data.puzzle);
      setIsSolved(false);
    } catch {
      console.log("Error fetching new puzzle");
    } finally {
      setIsGenerating(false);
    }
  }

  async function solvePuzzle() {
    setIsSolving(true);
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/solve_puzzle",
        board
      );
      setBoard(response.data.puzzle);
      setIsSolved(true);
    } catch {
      console.log("Error fetching new puzzle");
    } finally {
      setIsSolving(false);
    }
  }

  return (
    <div className="min-h-screen w-full flex flex-col items-center justify-center bg-gray-900">
      <h1 className="text-4xl font-semibold mb-6">AI - Sudoku Solver</h1>
      <div className="w-[520px] h-[520px] bg-gray-800 rounded-lg shadow-lg">
        <div className="grid grid-cols-9 gap-[2px] w-full h-full">
          {board.flat().map((value, index) => {
            return (
              <div
                key={index}
                className={`w-[55px] h-[55px] flex items-center justify-center text-white text-xl font-semibold bg-gray-700 border-2 ${
                  isSolved ? "border-green-500" : "border-red-500"
                } border-gray-600`}
              >
                {value !== 0 ? value : ""}
              </div>
            );
          })}
        </div>
      </div>
      <div className="flex items-center gap-4 mt-2">
        <button
          title="Start Solving"
          className={`cursor-pointer bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded mt-6 flex items-center transition duration-200 ease-in-out ${
            isSolving ? "pointer-events-none" : ""
          }`}
          onClick={solvePuzzle}
          disabled={isSolving}
        >
          {isSolving ? (
            <>
              <BsStars className="mr-2" /> AI is solving...
            </>
          ) : (
            <>
              <FaPlay className="mr-2" /> Start Solving
            </>
          )}
        </button>
        <button
          title="New Puzzle"
          className={`cursor-pointer bg-green-500 hover:bg-green-600 text-white font-medium py-2 px-4 rounded mt-6 flex items-center transition duration-200 ease-in-out ${
            isGenerating ? "pointer-events-none" : ""
          }`}
          onClick={getNewPuzzle}
          disabled={isGenerating}
        >
          {isGenerating ? (
            <>
              <BsStars className="mr-2" /> AI is generating...
            </>
          ) : (
            <>
              <FaGamepad className="mr-2" /> New Puzzle
            </>
          )}
        </button>
      </div>
    </div>
  );
};

export default SudokuBoard;
