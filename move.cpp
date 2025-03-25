#include "move.h"

bitset<64> ChessMove::destToBits(){
    bitset<64> move;
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            if(i == destY && j == destX){
                move.set(i * 8 + j);
            }
        }
    }
    return move;
}

bitset<64> ChessMove::originToBits(){
    bitset<64> move;
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            if(i == originY && j == originX){
                move.set(i * 8 + j);
            }
        }
    }
    return move;
}