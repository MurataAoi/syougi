
import requests
import shogi

board = shogi.Board()
sfen = board.sfen()
print("スタート")
def gikou(sfen):
    r = requests.get(
        url=f'https://17xn1ovxga.execute-api.ap-northeast-1.amazonaws.com/production/gikou?byoyomi=10000&position=sfen {sfen}')
    data = r.json()
    gikou_result = data['bestmove']
    return gikou_result


for i in range(100):
    prompt = f"{i + 1}手目："
    my_move = input(prompt)
    board.push_usi(my_move)
    gikou_move = gikou(board.sfen())
    print(gikou_move)
    board.push_usi(gikou_move)