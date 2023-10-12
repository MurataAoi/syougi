# ShogiPieceという名前の新しい駒を作成するためのクラスを定義します。
class ShogiPiece:
    def __init__(self, name, position):
        # 駒の名前と位置を設定します。
        self.name = name  # 駒の名前
        self.position = position  # 駒の現在の位置

    def legal_moves(self, board):
        # 駒の合法な動きを計算するためのメソッドです。
        moves = []  # 合法な動きのリスト

        # 駒の現在の位置を取得します。
        x, y = self.position

        if self.name == "歩":
            # 歩は前に1歩進むことができます。
            # まず、前方に進むことができるかどうかを確認します。
            if y > 0 and board[y - 1][x] is None:
                # 前方に進むことができる場合、その位置を動きのリストに追加します。
                moves.append((x, y - 1))

            # 最終段（敵陣）に達すると、斜め前に進むことができます。
            if y == 1:
                # 左前斜めに進むことができるかどうかを確認します。
                if x > 0 and board[y - 1][x - 1] is not None:
                    # 左前斜めに進むことができる場合、その位置を動きのリストに追加します。
                    moves.append((x - 1, y - 1))
                # 右前斜めに進むことができるかどうかを確認します。
                if x < 8 and board[y - 1][x + 1] is not None:
                    # 右前斜めに進むことができる場合、その位置を動きのリストに追加します。
                    moves.append((x + 1, y - 1))

        # 計算された合法な動きのリストを返します。
        return moves

# サンプルの将棋盤を作成します。将棋盤は9x9のリストで、各セルに駒が配置されているかNone（空）が入ります。
board = [[None for _ in range(9)] for _ in range(9)]

# 歩の例を作成します。歩の初期位置は (3, 3) です。
fu = ShogiPiece("歩", (3, 3))

# 歩の合法な動きを計算します。
legal_moves = fu.legal_moves(board)

# 合法な動きを表示します。
for move in legal_moves:
    print(f"歩 can move to {move}")
