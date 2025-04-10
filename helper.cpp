#include "helper.h"

ChessMove parseMove(string s, bool white){
    color side = white ? WHITE : BLACK;
    pieceType piece;
    switch (s[0])
    {
    case 'p':
        piece = PAWN;
        break;
    case 'n':
        piece = KNIGHT;
        break;
    case 'b':
        piece = BISHOP;
        break;
    case 'r':
        piece = ROOK;
        break;
    case 'q':
        piece = QUEEN;
        break;
    case 'k':
        piece = KING;
        break;
    default:
        break;
    }
    moveType move = NORMAL;
    int xval = s[1] - 'a';
    int yval = (s[2] - '1');
    int xdest = s[3] - 'a';
    int ydest = (s[4] - '1');
    cout << xval << " " << yval << " " << xdest << " " << ydest << endl;
    return ChessMove(xval, yval, xdest, ydest, piece, side);
}