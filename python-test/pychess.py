import chess
import chess.engine

# Set this to your Stockfish binary path
STOCKFISH_PATH = "stockfish"  # e.g., "./stockfish" or "C:\\path\\to\\stockfish.exe"

def evaluate_move(engine, board, move):
    
    board_copy = board.copy()
    result = engine.play(board_copy, chess.engine.Limit(depth=15))
    info_before = engine.analyse(board_copy, chess.engine.Limit(depth=15))
    score_before = info_before["score"].relative.score(mate_score=10000)

    board_copy.push(move)
    info_after = engine.analyse(board_copy, chess.engine.Limit(depth=15))
    score_after = info_after["score"].relative.score(mate_score=10000)

    if score_before is None or score_after is None:
        return "Unable to evaluate move."

    diff = (score_after - score_before)

    
    if result.move == move:
        feedback = "Best move"
    elif diff <= -300:
        feedback = "Blunder"
    elif diff <= -100:
        feedback = "Mistake"
    elif diff <= -50:
        feedback = "Inaccuracy"
    elif diff < 50:
        feedback = "OK move"
    elif diff < 150:
        feedback = "Good move"
    else:
        feedback = "Excellent move"

    return f"{feedback} (Δ {diff} cp). Best was {result.move.uci()}"

def main():
    board = chess.Board()
    print("You are White. Enter moves in UCI format (e.g., e2e4).\n")

    with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
        while not board.is_game_over():
            # Human move
            print(board)
            print("\nYour move.")
            try:
                move_input = input("Enter move (UCI): ").strip()
                move = chess.Move.from_uci(move_input)

                if move not in board.legal_moves:
                    print("Illegal move. Try again.\n")
                    continue
                boardCopy = board.copy()
                feedback = evaluate_move(engine, board, move)
                print(f"Your move: {move.uci()} ({board.san(move)})")
                print("hi")
                
                print(f"Feedback: {feedback}\n")
                board.push(move)


                

                if board.is_game_over():
                    break

            except Exception as e:
                print(f"Invalid input...: {e}\n")
                continue

            # Stockfish (Black) move
            print("Stockfish is thinking...\n")
            result = engine.play(board, chess.engine.Limit(depth=15))
            
            print(f"Stockfish played: {result.move.uci()} ({board.san(result.move)})\n")
            board.push(result.move)
        print(board)
        print("\nGame over.")
        print(f"Result: {board.result()}")

if __name__ == "__main__":
    main()
