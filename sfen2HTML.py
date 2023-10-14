import re


def insert_asterisks(input_string):
    # 正規表現を使用して数字を検出
    digits = re.findall(r"\d", input_string)

    result_string = input_string
    # 数字の数だけ '*' を挿入
    for digit in digits:
        result_string = result_string.replace(digit, "*" * int(digit), 1)

    return result_string


def sfen2HTML(sfen):
    piece_char = ""
    turn = ""
    td = ""
    tr = ""
    table = ""
    banmen = insert_asterisks(sfen.split(" ")[0])

    suji = 9
    dan_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    dan = 0
    for row in banmen.split("/"):
        td = ""
        for piece in row:
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

            if piece.islower():
                turn = "white"
            else:
                turn = "black"

            td += f"<td id='{suji}{dan_list[dan]}' onclick='SendIdAsPosition(this.id)'><span class='{turn}'>{piece_char}</span></td>"  # ここ？
            suji -= 1
        suji = 9
        tr = f"<tr>{td}</tr>"
        table += tr
        dan += 1
    table = f"<table class='board'><tbody>{table}</tbody></table>"
    return table

if __name__ == "__main__":
    print(sfen2HTML("lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1"))
