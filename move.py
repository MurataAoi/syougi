# # ShogiPieceという名前の新しい駒を作成するためのクラスを定義します。
# class ShogiPiece:
#     def __init__(self, name, position):
#         # 駒の名前と位置を設定します。
#         self.name = name  # 駒の名前
#         self.position = position  # 駒の現在の位置

#     def legal_moves(self, board):
#         # 駒の合法な動きを計算するためのメソッドです。
#         moves = []  # 合法な動きのリスト

#         # 駒の現在の位置を取得します。
#         x, y = self.position

#         if self.name == "歩":
#             # 歩は前に1歩進むことができます。
#             # まず、前方に進むことができるかどうかを確認します。
#             if y > 0 and board[y - 1][x] is None:
#                 # 前方に進むことができる場合、その位置を動きのリストに追加します。
#                 moves.append((x, y - 1))

#             # 最終段（敵陣）に達すると、斜め前に進むことができます。
#             if y == 1:
#                 # 左前斜めに進むことができるかどうかを確認します。
#                 if x > 0 and board[y - 1][x - 1] is not None:
#                     # 左前斜めに進むことができる場合、その位置を動きのリストに追加します。
#                     moves.append((x - 1, y - 1))
#                 # 右前斜めに進むことができるかどうかを確認します。
#                 if x < 8 and board[y - 1][x + 1] is not None:
#                     # 右前斜めに進むことができる場合、その位置を動きのリストに追加します。
#                     moves.append((x + 1, y - 1))

#         # 計算された合法な動きのリストを返します。
#         return moves

# # サンプルの将棋盤を作成します。将棋盤は9x9のリストで、各セルに駒が配置されているかNone（空）が入ります。
# board = [[None for _ in range(9)] for _ in range(9)]

# # 歩の例を作成します。歩の初期位置は (3, 3) です。
# fu = ShogiPiece("歩", (3, 3))

# # 歩の合法な動きを計算します。
# legal_moves = fu.legal_moves(board)

# # 合法な動きを表示します。
# for move in legal_moves:
#     print(f"歩 can move to {move}")


class ShogiPiece:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def legal_moves(self, board):
        moves = []
        x, y = self.position

        if self.name == "歩":
            if y > 0 and board[y - 1][x] is None:
                moves.append((x, y - 1))
            if y == 1:
                if x > 0 and board[y - 1][x - 1] is not None:
                    moves.append((x - 1, y - 1))
                if x < 8 and board[y - 1][x + 1] is not None:
                    moves.append((x + 1, y - 1))

        elif self.name == "香":
            for i in range(1, 9):
                if y - i < 0:
                    break
                if board[y - i][x] is not None:
                    break
                moves.append((x, y - i))

        elif self.name == "桂":
            # 桂馬の動きはL字形です。
            # 上に2マス進んでから斜めに進みます。
            if y > 1:
                if x > 0 and board[y - 2][x - 1] is None:
                    moves.append((x - 1, y - 2))
                if x < 7 and board[y - 2][x + 1] is None:
                    moves.append((x + 1, y - 2))

        elif self.name == "銀":
            # 銀将は斜めに進むことができます。
            if y > 0:
                if x > 0 and board[y - 1][x - 1] is None:
                    moves.append((x - 1, y - 1))
                if x < 8 and board[y - 1][x + 1] is None:
                    moves.append((x + 1, y - 1))
            # 後退も可能
            if y < 8:
                if board[y + 1][x] is None:
                    moves.append((x, y + 1))

        elif self.name == "金":
            # 金将は斜めと直進の移動ができます。
            if y > 0:
                if x > 0 and board[y - 1][x - 1] is None:
                    moves.append((x - 1, y - 1))
                if x < 8 and board[y - 1][x + 1] is None:
                    moves.append((x + 1, y - 1))
                if y < 8 and board[y + 1][x] is None:
                    moves.append((x, y + 1))

        elif self.name == "飛":
            # 飛車は直線的な動きができます。
            # 上に進む
            for i in range(1, 9):
                if y - i < 0:
                    break
                if board[y - i][x] is not None:
                    break
                moves.append((x, y - i))
            # 下に進む
            for i in range(1, 9):
                if y + i > 8:
                    break
                if board[y + i][x] is not None:
                    break
                moves.append((x, y + i))
            # 左に進む
            for i in range(1, 9):
                if x - i < 0:
                    break
                if board[y][x - i] is not None:
                    break
                moves.append((x - i, y))
            # 右に進む
            for i in range(1, 9):
                if x + i > 8:
                    break
                if board[y][x + i] is not None:
                    break
                moves.append((x + i, y))

        elif self.name == "角":
            # 角行は斜めの動きができます。
            # 左上に進む
            for i in range(1, 9):
                if x - i < 0 or y - i < 0:
                    break
                if board[y - i][x - i] is not None:
                    break
                moves.append((x - i, y - i))
            # 右上に進む
            for i in range(1, 9):
                if x + i > 8 or y - i < 0:
                    break
                if board[y - i][x + i] is not None:
                    break
                moves.append((x + i, y - i))
            # 左下に進む
            for i in range(1, 9):
                if x - i < 0 or y + i > 8:
                    break
                if board[y + i][x - i] is not None:
                    break
                moves.append((x - i, y + i))
            # 右下に進む
            for i in range(1, 9):
                if x + i > 8 or y + i > 8:
                    break
                if board[y + i][x + i] is not None:
                    break
                moves.append((x + i, y + i))

        elif self.name == "玉":
            # 玉将は斜めと直進の移動ができますが、1マスだけです。
            # 上に進む
            if y > 0:
                moves.append((x, y - 1))
            # 下に進む
            if y < 8:
                moves.append((x, y + 1))
            # 左に進む
            if x > 0:
                moves.append((x - 1, y))
            # 右に進む
            if x < 8:
                moves.append((x + 1, y))
            # 左上に進む
            if x > 0 and y > 0:
                moves.append((x - 1, y - 1))
            # 右上に進む
            if x < 8 and y > 0:
                moves.append((x + 1, y - 1))
            # 左下に進む
            if x > 0 and y < 8:
                moves.append((x - 1, y + 1))
            # 右下に進む
            if x < 8 and y < 8:
                moves.append((x + 1, y + 1))

        return moves


# # サンプルの将棋盤を作成
# board = [[None for _ in range(9)] for _ in range(9)]

# 各駒の例を作成
# fu = ShogiPiece("歩", (3, 3))
# kyosha = ShogiPiece("香", (3, 3))
# keima = ShogiPiece("桂", (3, 3))
# gin = ShogiPiece("銀", (3, 3))
# kin = ShogiPiece("金", (3, 3))
# hisha = ShogiPiece("飛", (3, 3))
# kakugyo = ShogiPiece("角", (3, 3))
# gyokusho = ShogiPiece("玉", (3, 3))

# # 各駒の合法な動きを計算し、表示
# legal_moves_fu = fu.legal_moves(board)
# legal_moves_kyosha = kyosha.legal_moves(board)
# legal_moves_keima = keima.legal_moves(board)
# legal_moves_gin = gin.legal_moves(board)
# legal_moves_kin = kin.legal_moves(board)
# legal_moves_hisha = hisha.legal_moves(board)
# legal_moves_kakugyo = kakugyo.legal_moves(board)
# legal_moves_gyokusho = gyokusho.legal_moves(board)

# print("歩の合法な動き:")
# for move in legal_moves_fu:
#     print(f"歩 can move to {move}")

# print("香の合法な動き:")
# for move in legal_moves_kyosha:
#     print(f"香 can move to {move}")

# print("桂の合法な動き:")
# for move in legal_moves_keima:
#     print(f"桂 can move to {move}")

# print("銀の合法な動き:")
# for move in legal_moves_gin:
#     print(f"銀 can move to {move}")

# print("金の合法な動き:")
# for move in legal_moves_kin:
#     print(f"金 can move to {move}")

# print("飛車の合法な動き:")
# for move in legal_moves_hisha:
#     print(f"飛車 can move to {move}")

# print("角行の合法な動き:")
# for move in legal_moves_kakugyo:
#     print(f"角行 can move to {move}")

# print("玉将の合法な動き:")
# for move in legal_moves_gyokusho:
#     print(f"玉将 can move to {move}")
