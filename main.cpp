#include "util.h"
#include "board.h"
#include "move.h"
#include "helper.h"
#include "board.cpp"
#include "move.cpp"
#include "helper.cpp"
#include <iostream>
//using namespace std;

int main() {
    Board board;
    board.printBoard();
    bool whiteTurn = true;
    while(true){
        string input;
        cout << "Enter move: ";
        cin >> input;
        ChessMove move = parseMove(input, whiteTurn);
        if(move.type() == PROMOTION){
            //prompt user for promotion
        }
        if(board.isLegal(move)){
            board.makeMove(move);
        }
        else{
            cout << "Illegal move" << endl;
        }
        whiteTurn = !whiteTurn;
        board.printBoard();
    }
}