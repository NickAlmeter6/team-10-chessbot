#include "board.h"

Board::Board(){
    whitePawns = 0x000000000000FF00;
    blackPawns = 0x00FF000000000000;
    whiteKnights = 0x0000000000000042;
    blackKnights = 0x4200000000000000;
    whiteBishops = 0x0000000000000024;
    blackBishops = 0x2400000000000000;
    whiteRooks = 0x0000000000000081;
    blackRooks = 0x8100000000000000;
    whiteQueens = 0x0000000000000008;
    blackQueens = 0x0800000000000000;
    whiteKing = 0x0000000000000010;
    blackKing = 0x1000000000000000;
}

bool isLegal(ChessMove move){
    bitset<64> square = move.originToBits();
    
    move.destToBits();
}

void Board::printBoard(){
    cout << "  a b c d e f g h" << endl;
    for(int i = 0; i < 8; i++){
        cout << 8 - i << " ";
        for(int j = 0; j < 8; j++){
            int index = i * 8 + j;
            if(whitePawns[index]){
                cout << "P ";
            }else if(blackPawns[index]){
                cout << "p ";
            }else if(whiteKnights[index]){
                cout << "N ";
            }else if(blackKnights[index]){
                cout << "n ";
            }else if(whiteBishops[index]){
                cout << "B ";
            }else if(blackBishops[index]){
                cout << "b ";
            }else if(whiteRooks[index]){
                cout << "R ";
            }else if(blackRooks[index]){
                cout << "r ";
            }else if(whiteQueens[index]){
                cout << "Q ";
            }else if(blackQueens[index]){
                cout << "q ";
            }else if(whiteKing[index]){
                cout << "K ";
            }else if(blackKing[index]){
                cout << "k ";
            }else{
                cout << ". ";
            }
        }
        cout << endl;
    }
}