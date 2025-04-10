#include "board.h"

Board::Board(){
    pieces[0] = 0x000000000000FF00; //white pawns
    pieces[1] = 0x00FF000000000000; //black pawns
    pieces[2] = 0x0000000000000042; //white knights
    pieces[3] = 0x4200000000000000; //black knights
    pieces[4] = 0x0000000000000024; //white bishops
    pieces[5] = 0x2400000000000000; //black bishops
    pieces[6] = 0x0000000000000081; //white rooks
    pieces[7] = 0x8100000000000000; //black rooks
    pieces[8] = 0x0000000000000008; //white queens
    pieces[9] = 0x0800000000000000; //black queens
    pieces[10] = 0x0000000000000010; //white king
    pieces[11] = 0x1000000000000000; //black king
}

bool Board::isLegal(ChessMove move){
    bitset<64> square = move.originToBits();
    int index = move.getPiece() * 2 + move.getSide();
    int space;
     
    if((square & pieces[index]) == 0){
        return false;
    }
        

    move.destToBits();
    return true;
}

void Board::makeMove(ChessMove move){
    
    if(move.type() == CASTLE){
        if(move.getSide() == WHITE){
            if(true){ //kingside
                pieces[10] &= ~0x0000000000000001;
                pieces[10] |= 0x0000000000000040;
                pieces[6] &= ~0x0000000000000080;
                pieces[6] |= 0x0000000000000020;
            }else{
                pieces[10] &= ~0x0000000000000100;
                pieces[10] |= 0x0000000000000004;
                pieces[6] &= ~0x0000000000000001;
                pieces[6] |= 0x0000000000000008;
            }
        }else{
            if(true){
                pieces[11] &= ~0x0000000000000001;
                pieces[11] |= 0x0000000000000040;
                pieces[7] &= ~0x0000000000000080;
                pieces[7] |= 0x0000000000000020;
            }else{
                pieces[11] &= ~0x0000000000000100;
                pieces[11] |= 0x0000000000000004;
                pieces[7] &= ~0x0000000000000001;
                pieces[7] |= 0x0000000000000008;
            }
        }
    }
    else{
        bitset<64> square = move.originToBits();
    bitset<64> dest = move.destToBits();
    int index = move.getPiece() * 2 + move.getSide();
    pieces[index] &= ~square;
    pieces[index] |= dest;
    }
}

void Board::printBoard(){
    cout << "  a b c d e f g h" << endl;
    for(int i = 7; i >= 0; i--){
        cout << i+1 << " ";
        for(int j = 0; j < 8; j++){
            int index = i * 8 + j;
            if(pieces[0].test(index)){
                cout << "P ";
            }
            else if (pieces[1].test(index)){
                cout << "p ";
            }
            else if (pieces[2].test(index)){
                cout << "N ";
            }
            else if (pieces[3].test(index)){
                cout << "n ";
            }
            else if (pieces[4].test(index)){
                cout << "B ";
            }
            else if (pieces[5].test(index)){
                cout << "b ";
            }
            else if (pieces[6].test(index)){
                cout << "R ";
            }
            else if (pieces[7].test(index)){
                cout << "r ";
            }
            else if (pieces[8].test(index)){
                cout << "Q ";
            }
            else if (pieces[9].test(index)){
                cout << "q ";
            }
            else if (pieces[10].test(index)){
                cout << "K ";
            }
            else if (pieces[11].test(index)){
                cout << "k ";
            }
            else{
                cout << ". ";
            }
        }
        cout << endl;
    }
}

bitset<64> Board::getOccupied(){
    bitset<64> compound = 0;
    for(int i = 0; i < 12; i++){
        compound |= pieces[i];
    }
    return compound;
}

bitset <64> Board::getWhite(){
    bitset<64> compound = 0;
    for(int i = 0; i < 12; i+=2){
        compound |= pieces[i];
    }
    return compound;
}

bitset <64> Board::getBlack(){
    bitset<64> compound = 0;
    for(int i = 1; i < 12; i+=2){
        compound |= pieces[i];
    }
    return compound;
}