the_board_test_1 = {
    '1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '2a': "bpawn", '2b': "bpawn", '3a': "bpawn"
}

the_board_test_2 = {
    '1h': 'bking', '2h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '2a': "bpawn", '2b': "bpawn", '3a': "bpawn"
}

the_board_test_3 = {
    '1h': 'bking', '10j': 'ppawn', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '2a': "bpawn", '2b': "bpawn", '3a': "bpawn"
}

def is_valid_chess_board(board):
    pieces = board.values()

    pieces_count = {}

    for piece in pieces:
        pieces_count.setdefault(piece, 0)
        pieces_count[piece] += 1
        
    is_number_of_pieces_ok = check_number_of_pieces(pieces_count)
    b_and_w_pieces_number = check_black_and_white_pieces(pieces_count)
    are_position_ok = check_for_position(board)

    if is_number_of_pieces_ok and b_and_w_pieces_number and are_position_ok:
        return True
    
    return False

def check_number_of_pieces(pieces_obj):
    # Check for number of pieces
    for k,v in pieces_obj.items():
        if (k == 'wking' or k == 'bking' or k == 'bqueen' or k == 'wqueen') and v > 1:
            return False
        elif (k == 'wpawns' or k == 'bpawns') and v > 8:
            return False
        elif (k == 'wbishop' or k == 'bbishop') and v > 2:
            return False
        elif (k == 'wrock' or k == 'brock') and v > 2:
            return False
        elif (k == 'wknigh' or k == 'bknight') and v > 2:
            return False
    
    return True

def check_black_and_white_pieces(pieces_obj):
    # Check for white pieces and black pieces count
    b_pieces = 0
    w_pieces = 0
    for piece in pieces_obj.keys():
        if piece[0] == "w":
            w_pieces += 1
        else:
            b_pieces += 1

        if b_pieces > 16 or w_pieces > 16:
            return False
    return True

def check_for_position(board):
    positions = board.keys()

    for pos in positions:
        if (0 < int(pos[0]) < 9) and ('a' <= pos[1] <= 'z'):
            continue
        else:
            return False
    
    return True

print(is_valid_chess_board(the_board_test_1))
print(is_valid_chess_board(the_board_test_2))
print(is_valid_chess_board(the_board_test_3))