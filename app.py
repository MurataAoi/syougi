from flask import Flask, render_template
from sfen2HTML import sfen2HTML
# from move import ShogiPiece
import shogi
import re

app = Flask(__name__)

board = shogi.Board()


sfen = board.sfen()




@app.route("/")
def index():
    banmen = sfen2HTML(sfen)
    return render_template("board.html", banmen=banmen)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)