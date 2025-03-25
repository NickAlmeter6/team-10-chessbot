#ifndef MOVE_H
#define MOVE_H
#include "util.h"
class ChessMove{
    private:
        char originX;
        char originY;
        char destX;
        char destY;
    public:
        bitset<64> destToBits();
        bitset<64> originToBits();

};
#endif