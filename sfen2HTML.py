import re

def insert_asterisks(input_string):
    # 正規表現を使用して数字を検出
    digits = re.findall(r"\d", input_string)

    result_string = input_string
    # 数字の数だけ '*' を挿入
    for digit in digits:
        result_string = result_string.replace(digit, "*" * int(digit), 1)

    return result_string


def sfen2piece(piece):
    if piece == "*":
        piece_char = ""
    elif piece in ["l", "L"]:
        piece_char = "香"
    elif piece in ["n", "N"]:
        piece_char = "桂"
    elif piece in ["s", "S"]:
        piece_char = "銀"
    elif piece in ["g", "G"]:
        piece_char = "金"
    elif piece in ["k", "K"]:
        piece_char = "王"
    elif piece in ["r", "R"]:
        piece_char = "飛"
    elif piece in ["b", "B"]:
        piece_char = "角"
    elif piece in ["p", "P"]:
        piece_char = "歩"
    
    else:
        piece_char = ""
    
    return piece_char


def sfen2piece_promotion(piece):
    piece_char = ""
    if piece in ["l", "L"]:
        piece_char = "杏"
    elif piece in ["n", "N"]:
        piece_char = "圭"
    elif piece in ["s", "S"]:
        piece_char = "全"
    elif piece in ["r", "R"]:
        piece_char = "龍"
    elif piece in ["b", "B"]:
        piece_char = "馬"
    elif piece in ["p", "P"]:
        piece_char = "と"
    return piece_char


def sfen2HTML(sfen):
    piece_char = ""
    turn = ""
    td = ""
    tr = ""
    table = ""
    banmen = insert_asterisks(sfen.split(" ")[0])
    mochigoma = insert_asterisks(sfen.split(" ")[2])
    mochigoma_w_list = []
    mochigoma_b_list = []
    mochigoma_tr_w_piece = ""
    mochigoma_tr_b_piece = ""
    mochigoma_tr_w_count = ""
    mochigoma_tr_b_count = ""
    mochigoma_tr_w = ""
    mochigoma_tr_b = ""
    for i in mochigoma:
        if i.islower():
            mochigoma_w_list.append(i)
        else:
            mochigoma_b_list.append(i)

    mochigoma_piece_list_w = ["p", "l", "n", "s", "G", "r", "b", ]
    mochigoma_piece_list_b = ["P", "L", "N", "S", "G", "R", "B"]
    for i in range(len(mochigoma_piece_list_w)):
        mochigoma_tr_w_piece += f"<td id='{mochigoma_piece_list_b[i]}*' onclick='SendIdAsPosition(this.id)'>{sfen2piece(mochigoma_piece_list_w[i])}</td>"
        mochigoma_tr_b_piece += f"<td id='{mochigoma_piece_list_b[i]}*' onclick='SendIdAsPosition(this.id)'>{sfen2piece(mochigoma_piece_list_b[i])}</td>"
    mochigoma_tr_w_piece = "<tr>" + mochigoma_tr_w_piece + "</tr>"
    mochigoma_tr_b_piece = "<tr>" + mochigoma_tr_b_piece + "</tr>"
    for i in range(len(mochigoma_piece_list_w)):
        mochigoma_tr_w_count += f"<td>{mochigoma_w_list.count(mochigoma_piece_list_w[i])}</td>"
        mochigoma_tr_b_count += f"<td>{mochigoma_b_list.count(mochigoma_piece_list_b[i])}</td>"
    mochigoma_tr_w_count = "<tr>" + mochigoma_tr_w_count + "</tr>"
    mochigoma_tr_b_count = "<tr>" + mochigoma_tr_b_count + "</tr>"
    mochigoma_tr_w = f"<table id='mochigoma_w' class='board'>{mochigoma_tr_w_piece}{mochigoma_tr_w_count}</table>"
    mochigoma_tr_b = f"<table id='mochigoma_b' class='board'>{mochigoma_tr_b_piece}{mochigoma_tr_b_count}</table>"

    suji = 9
    dan_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    dan = 0
    promotion = False
    for row in banmen.split("/"):
        td = ""
        for piece in row:
            if piece == "+":
                promotion = True
                continue
            elif promotion:
                piece_char = sfen2piece_promotion(piece)
                promotion = False
            else:
                piece_char = sfen2piece(piece)

            if piece.islower():
                turn = "white"
            else:
                turn = "black"

            td += f"<td id='{suji}{dan_list[dan]}' onclick='SendIdAsPosition(this.id)'><span class='{turn}'>{piece_char}</span></td>"
            suji -= 1
        suji = 9
        tr = f"<tr>{td}</tr>"
        table += tr
        dan += 1
    table = f"<table id='banmen' class='board'><tbody>{table}</tbody></table>"
    return [table, mochigoma_tr_w, mochigoma_tr_b]


if __name__ == "__main__":
    print(sfen2HTML("ln+sg1g1nl/1r3k1s1/pp1ppp1pp/2p3p2/9/9/PP1PPPPPP/7R1/LNSGKGSNL b Bbp 9")[0])