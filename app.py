import json
from flask import Flask, render_template, request
from sfen2HTML import sfen2HTML
from move import ShogiPiece

# from finish import
import shogi
import re

app = Flask(__name__)

sfen = shogi.Board().sfen()


# @app.route("/")
# def index():
#     banmen = sfen2HTML(sfen)
#     return render_template("board.html", banmen=banmen)


@app.route("/")
def board_func():
    # move_piece = ShogiPiece("歩", (3, 3))  # ShogiPiece クラスのインスタンスを作成
    # board = [[None for _ in range(9)] for _ in range(9)]  # サンプルの将棋盤
    # legal_moves = move_piece.legal_moves(board)  # 歩の動きを取得
    # print(legal_moves)

    banmen = sfen2HTML(sfen)
    return render_template("board.html", banmen=banmen)

@app.route("/call_from_ajax", methods=["POST"])
def callfromajax():
    dict = {}
    if request.method == "POST":
        try:
            masu = request.form["masu"]
        except Exception as e:
            masu = str(e)
        dict = {"answer": masu}
    return json.dumps(dict)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
