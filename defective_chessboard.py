import numpy as np

__all__ = ["createDefectiveChessboard"]


def createDefectiveChessboard(size=16, dr=3, dc=3):
    return DC(size, dr, dc)


class DC:
    def __init__(self, size, dr, dc):
        """

        :param size: the size of the chessboard size = 2 ^ n
        :param dr: the row of the defective point
        :param dc: the column of the defective point
        :return:
        """
        self.size = size
        self.dr = dr
        self.dc = dc
        self.chessboard = np.zeros((size, size))
        self.tile = 0
        self.size = size

    def show(self):
        # 这里是控制台版的show，我先把它注释了
        self.tile_board(0, 0, self.dr, self.dc, self.size)
        for i in range(self.size):
            for j in range(self.size):
                print('%5d' % int(self.chessboard[i][j]), end='')
            print("\n")
        pass

    def tile_board(self, tr, tc, dr, dc, size):
        tr = int(tr)
        tc = int(tc)
        dr = int(dr)
        dc = int(dc)
        if size == 1:
            return
        self.tile += 1
        t = self.tile
        s = size // 2
        if dr < tr + s and dc < tc + s:
            self.tile_board(tr, tc, dr, dc, s)
        else:
            self.chessboard[tr + s - 1][tc + s - 1] = t
            self.tile_board(tr, tc, tr + s - 1, tc + s - 1, s)
        if dr < tr + s and dc >= tc + s:
            self.tile_board(tr, tc + s, dr, dc, s)
        else:
            self.chessboard[tr + s - 1][tc + s] = t
            self.tile_board(tr, tc + s, tr + s - 1, tc + s, s)
        if dr >= tr + s and dc < tc + s:
            self.tile_board(tr + s, tc, dr, dc, s)
        else:
            self.chessboard[tr + s][tc + s - 1] = t
            self.tile_board(tr + s, tc, tr + s, tc + s - 1, s)
        if dr >= tr + s and dc >= tc + s:
            self.tile_board(tr + s, tc + s, dr, dc, s)
        else:
            self.chessboard[tr + s][tc + s] = t
            self.tile_board(tr + s, tc + s, tr + s, tc + s, s)

        return self.chessboard
