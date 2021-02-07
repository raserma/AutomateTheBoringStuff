#!/usr/bin/env python3

# A valid board will have exactly:
#   - 1 Black King & 1 White King
#   - 16 pieces per player
#   - 8 pawns per player
#   - all pieces must be on a valid space from '1a' to '8h'
#   - the piece names begin with either `w` or `b`, followed by
#   `pawn`,'knight', 'bishop', 'rook', 'queen', or 'king'
#
# It assumes the input board is syntactically correct, i.e:
# the board doesn't contain strange values to break the program.
# (program could be improved to catch such type exceptions)

# Note: There are many ways of doing this exercise.

def is_valid_chess_board(chess_board):
    """Validates a chess board"""

    # Initialize the counts
    pieces_count = {'b': 0, 'w': 0}
    pawn_count = {'b': 0, 'w': 0}
    king_count = {'b': 0, 'w': 0}

    # Define the model
    piece_type = ('king', 'queen', 'rook', 'knight', 'bishop', 'pawn')
    color_type = ('b', 'w')

    for pos, i in chess_board.items():
        # -*- check pieces keys -*-
        # all pieces must be on a valid space from '1a' to '8h'
        if int(pos[0]) > 8:
            print('ERROR: Invalid piece key. All pieces must be on a valid space from \'1a\' to \'8h\'')
            return False
        if str(pos[1]) > 'h':
            print('ERROR: Invalid piece key. All pieces must be on a valid space from \'1a\' to \'8h\'')
            return False

        # piece values can be empty
        if i != '':
            # -*- get the piece value -*-
            this_piece = i[1:]
            this_color = i[0]

            # add a new piece
            pieces_count[this_color] += 1
            if pieces_count[this_color] > 16:
                print('ERROR: Too many ' + this_color + ' total pieces')
                return False

            # -*- check pieces values -*-
            # is the wrong piece type?
            if this_piece not in piece_type:
                print('ERROR: ' + this_piece + ' is an invalid piece type')
                return False
            # is a king?
            elif this_piece == 'king':
                king_count[this_color] += 1
                # more than one?
                if king_count[this_color] > 1:
                    print('ERROR: Too many ' + this_color + ' kings')
                    return False
            # is a pawn?
            elif this_piece == 'pawn':
                pawn_count[this_color] += 1
                # more than 8?
                if pawn_count[this_color] > 8:
                    print('ERROR: Too many ' + this_color + ' pawns')
                    return False

            # is either white or black color?
            if this_color not in color_type:
                print('ERROR: No White or Black color')
                return False

    print('The chess board is validated.')
    return True


if __name__ == '__main__':

    board = {'1a': 'bpawn', '2a': '', '18a': 'bking', '4a': 'brook',
             '5a': '', '6a': 'bknight', '7a': 'bbishop', '8a': 'bbishop',
             '1b': 'bpawn', '2b': 'bpawn', '3b': 'bpawn', '4b': 'bpawn',
             '5b': 'bpawn', '6b': '', '7b': 'bpawn', '8b': 'brook',
             '1c': '', '2c': 'wqueen', '3c': 'wrook', '4c': 'wrook',
             '5c': 'wbishop', '6c': '', '7c': 'wknight', '8c': 'wknight',
             '1e': '', '2e': 'wpawn', '3e': 'wpawn', '4e': 'wpawn',
             '5e': 'wpawn', '6e': 'wpawn', '7e': 'wpawn', '8e': 'wpawn',
             '1f': '', '2f': '', '3f': '', '4f': 'bqueen', '5f': '', '6f': '', '7f': '', '8f': '',
             '1g': '', '2g': 'wking', '3g': '', '4g': '', '5g': '', '6g': '', '7g': '', '8g': '',
             '1h': 'bknight', '2h': 'wpawn', '3h': 'wbishop', '4h': '', '5h': 'bpawn', '6h': '', '7h': '', '8h': '', }
    print('Board is validated? %s' % (is_valid_chess_board(board)))
