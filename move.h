#ifndef MOVE_H
#define MOVE_H
#include "util.h"
class ChessMove{
    private:
        //TODO: refactor to byte array
        char originX;
        char originY;
        char destX;
        char destY;
        pieceType piece;
        color side;
        moveType move;
    public:
        ChessMove(char originX, char originY, char destX, char destY, pieceType piece, color side);
        bitset<64> destToBits();
        bitset<64> originToBits();
        color getSide() {return side;};
        pieceType getPiece() {return piece;};
        char index(){return destY * 8 + destX;};
        moveType type() {return move;};
};
#endif