from flask import Flask, render_template
from sfen2HTML import sfen2HTML
from move import ShogiPiece
import shogi
import re

app = Flask(__name__)

board = shogi.Board()
# board.push_usi("3g3f")

sfen = board.sfen()


@app.route("/")
def index():
    banmen = sfen2HTML(sfen)
    return render_template("board.html", banmen=banmen)


@app.route("/")
def board_func():
    move_piece = ShogiPiece("歩", (3, 3))  # ShogiPiece クラスのインスタンスを作成
    board = [[None for _ in range(9)] for _ in range(9)]  # サンプルの将棋盤
    legal_moves = move_piece.legal_moves(board)  # 歩の動きを取得
    print(legal_moves)

    banmen = sfen2HTML(sfen)
    return render_template("board.html", banmen=banmen)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
