import json
from flask import Flask, render_template, request, flash, session, redirect, url_for
from sfen2HTML import sfen2HTML
from gikou import gikou_return
import shogi


class Board:

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
app.secret_key = "shogi"

board = ""
sfen = ""


@app.route("/", methods=["GET","POST"])
def board_func():
    banmen = sfen2HTML(game.sfen)
    if request.method == "GET":
        return render_template("board.html", syogiban=banmen[0], mochigoma_w=banmen[1], mochigoma_b=banmen[2])
    elif request.method == "POST":
        
        flash("テキストを入力してください。", "promote")

        return render_template("board.html", syogiban=banmen[0], mochigoma_w=banmen[1], mochigoma_b=banmen[2])

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
            dict = {"banmen": ""}
            return json.dumps(dict)
        
        elif pieceWasSelected is True:
            after_move = masu
            pieceWasSelected = False
            if shogi.Move.from_usi(before_move + after_move) not in game.board.legal_moves:
                dict = {"banmen": ""}
                return json.dumps(dict)
            else:
                game.cyakusyu(before_move + after_move)
                before_move = ""
                dict = {
                    "banmen": sfen2HTML(game.sfen)[0],
                    "mochigoma_w": sfen2HTML(game.sfen)[1],
                    "mochigoma_b": sfen2HTML(game.sfen)[2],
                    "message": "技巧考え中"
                }
                return json.dumps(dict)


@app.route("/gikou", methods=["POST"])
def gikou():
    if request.method == "POST":
        print("技巧に与えているsfen" + game.sfen)
        gikoumove = gikou_return(game.sfen)
        print(gikoumove)
        game.cyakusyu(gikoumove)
        print("技巧着手後sfen" + game.sfen)
        dict = {
            "banmen": sfen2HTML(game.sfen)[0],
            "mochigoma_w": sfen2HTML(game.sfen)[1],
            "mochigoma_b": sfen2HTML(game.sfen)[2],
            "message": "あなたのばんです！"
        }

        return json.dumps(dict)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)