# class ShogiBoard:
#     def __init__(self):
#         # 初期盤面の設定
#         self.board = [
#             [" ", " ", " ", " ", "k", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
#             [" ", " ", " ", " ", "K", " ", " ", " ", " "]
#         ]

#     def is_king_captured(self):
#         opponent_king = False
#         your_king = False

#         for row in self.board:
#             if "k" in row:
#                 opponent_king = True
#             if "K" in row:
#                 your_king = True

#         if opponent_king and your_king:
#             return "相手の玉と自分の玉が取られました"
#         elif opponent_king:
#             return "相手の玉を取りました"
#         elif your_king:
#             return "自分の玉が取られました"
#         else:
#             return "相手の玉と自分の玉はまだ取られていません"

#     def display_board(self):
#         for row in self.board:
#             print(" ".join(row))

# # ゲームのインスタンスを作成
# game = ShogiBoard()
# game.display_board()
# result = game.is_king_captured()
# print(result)
