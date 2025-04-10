#include <bitset>
#include <iostream>

#ifndef UTIL_H
#define UTIL_H
enum pieceType{
    PAWN,
    KNIGHT,
    BISHOP,
    ROOK,
    QUEEN,
    KING,
    UNKOWN
};
enum color{
    WHITE,
    BLACK
};
enum moveType{
    NORMAL,
    CASTLE,
    ENPASSANT,
    PROMOTION
};
using namespace std;
#endif