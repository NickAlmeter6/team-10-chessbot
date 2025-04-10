#include "move.h"
ChessMove::ChessMove(char originX, char originY, char destX, char destY, pieceType piece, color side){
    this->originX = originX;
    this->originY = originY;
    this->destX = destX;
    this->destY = destY;
    this->piece = piece;
    this->side = side;
}
bitset<64> ChessMove::destToBits(){
    bitset<64> move;
    // for(int i = 0; i < 8; i++){
    //     for(int j = 0; j < 8; j++){
    //         if(i == destY && j == destX){
                
    //         }
    //     }
    // }
    move.set( destY * 8 + destX);
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
    move.set( originX * 8 + originY);
    return move;
}


