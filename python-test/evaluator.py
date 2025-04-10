import chess
import chess.engine
import multiprocessing
import time
import importlib
import sys

# Motions in desired order
motions = [
    "start",
    "your_turn",
    "Thinking",     # Infinite loop
    "plain_move",
    "good_job",
    "big_plunge",
    "you_win",
    "I_win"         # Infinite loop (wrist rotate)
]
def run_module(name):
    try:
        mod = importlib.import_module(name)
        if hasattr(mod, 'main'):
            mod.main()
        else:
            print(f"Module '{name}' has no main() function.")
    except Exception as e:
        print(f"Error running {name}: {e}")

def run_with_timeout(name, timeout):
    print("jhbubjh")
    process = multiprocessing.Process(target=run_module, args=(name,))
    process.start()
    process.join(timeout)

    if process.is_alive():
        print(f"Timeout reached. Terminating '{name}'...")
        process.terminate()
        process.join()
    else:
        print(f"'{name}' completed.")

def evaluate_move(fen, move_str):
    board = chess.Board(fen)
    board_copy = board.copy()
    board.push_san(move_str)

    # Example with Stockfish
    with chess.engine.SimpleEngine.popen_uci("stockfish") as engine:
        result = engine.play(board_copy, chess.engine.Limit(depth=15))
        info_before = engine.analyse(board_copy, chess.engine.Limit(depth=15))
        score_before = info_before["score"].relative.score(mate_score=10000)

        info_after = engine.analyse(board, chess.engine.Limit(depth=15))
        score_after = info_after["score"].relative.score(mate_score=10000)

        if score_before is None or score_after is None:
            return "Unable to evaluate move."

        diff = (score_after - score_before)


        if board_copy.san(result.move) == move_str:
            run_with_timeout("good_job", timeout=3)
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
        print(feedback)
        cpumove = engine.play(board, chess.engine.Limit(time=0.1))
        return cpumove.move.uci()
