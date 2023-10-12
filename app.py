from flask import Flask, render_template
from move import ShogiPiece  # ShogiPiece クラスをインポート

app = Flask(__name__)

@app.route("/")
def board():
    move_piece = ShogiPiece("歩", (3, 3))  # ShogiPiece クラスのインスタンスを作成
    board = [[None for _ in range(9)] for _ in range(9)]  # サンプルの将棋盤
    legal_moves = move_piece.legal_moves(board)  # 歩の動きを取得
    return render_template("board.html")

if __name__ == "__main__":
    app.run()
