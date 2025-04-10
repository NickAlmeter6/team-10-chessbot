import React, { useState } from "react";
import { Chess } from "chess.js";
import { Chessboard } from "react-chessboard";
import { evaluateMove } from "./api";

const Board = () => {
  const [game, setGame] = useState(new Chess());

//   const makeAMove = (move) => {
//     console.log("Move:", move);
//     const gameCopy = new Chess(game.fen());
//     console.log("Game Copy:", gameCopy.fen());
//     const result = gameCopy.move(move);
//     console.log("Game Copy:", gameCopy.fen());
//     if (result) setGame(gameCopy);
//     return result;
//   };

  const onDrop = async (sourceSquare, targetSquare) => {
    const move = {
      from: sourceSquare,
      to: targetSquare,
      promotion: "q",
    };
  
    const gameCopy = new Chess(game.fen());
    const oldCopy = new Chess(game.fen());
    const result = gameCopy.move(move);
    console.log("Game Copy:", gameCopy.fen());
  
    if (!result) return false;
  
    // Now gameCopy is the updated position after player move
    // We use it immediately to send to backend
    console.log(gameCopy.fen(), result.san)
    const response = await evaluateMove(oldCopy.fen(), result.san);
  
    if (response?.bot_move) {
      // Apply bot move to gameCopy
      gameCopy.move({
        from: response.bot_move.slice(0, 2),
        to: response.bot_move.slice(2, 4),
        promotion: "q",
      });
  
      // Only update state after both moves are done
      setGame(gameCopy);
    } else {
      setGame(gameCopy); // Only player move happened
    }
  
    return true;
  };
  

  return <Chessboard position={game.fen()} onPieceDrop={onDrop} />;
};

export default Board;
