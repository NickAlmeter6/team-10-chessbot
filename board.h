#ifndef BOARD_H
#define BOARD_H

#include "util.h"
#include "move.h"
#include <bitset>
class Board{
    private:
        bitset<64> whitePawns;
        bitset<64> blackPawns;

        bitset<64> whiteKnights;
        bitset<64> blackKnights;

        bitset<64> whiteBishops;
        bitset<64> blackBishops;

        bitset<64> whiteRooks;
        bitset<64> blackRooks;

        bitset<64> whiteQueens;
        bitset<64> blackQueens;

        bitset<64> whiteKing;
        bitset<64> blackKing;

        bitset<64> pieces [12];
    public:
        Board();
        void printBoard();
        bool isLegal(ChessMove move);
        void makeMove(ChessMove move);
        bitset<64> getOccupied();
};
#endif