import json
from flask import Flask, render_template, request
from sfen2HTML import sfen2HTML
from gikou import gikou_return

# from finish import
import shogi


class Board:
    """"""

    def __init__(self):
        self.board = shogi.Board()
        self.sfen = self.board.sfen()

    def cyakusyu(self, usi):
        self.board.push_usi(usi)
        self.sfen = self.board.sfen()
        return sfen


game = Board()

pieceWasSelected = False
before_move = ""

app = Flask(__name__)

board = ""
sfen = ""


@app.route("/")
def board_func():
    banmen = sfen2HTML(game.sfen)

    return render_template("board.html", banmen=banmen)


@app.route("/call_from_ajax", methods=["POST"])
def callfromajax():
    global pieceWasSelected
    global before_move

    dict = {}
    if request.method == "POST":
        try:
            masu = request.form["masu"]
        except Exception as e:
            masu = str(e)

        if not pieceWasSelected:
            before_move = masu
            pieceWasSelected = True
            print("piece selected")
            dict = {"answer": ""}
            return json.dumps(dict)

        elif pieceWasSelected is True:
            after_move = masu
            pieceWasSelected = False
            game.cyakusyu(before_move + after_move)
            before_move = ""
            dict = {"answer": sfen2HTML(game.sfen)}
            return json.dumps(dict)


@app.route("/gikou", methods=["POST"])
def gikou():
    if request.method == "POST":
        print("技巧に与えているsfen" + game.sfen)
        gikoumove = gikou_return(game.sfen)
        print(gikoumove)
        game.cyakusyu(gikoumove)
        print("技巧着手後sfen" + game.sfen)
        dict = {"gikoureturn": sfen2HTML(game.sfen)}
        return json.dumps(dict)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
