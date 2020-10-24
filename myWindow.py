from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui import Ui_MainWindow
from defective_chessboard import DC

import numpy as np

# 随机生成包含N个数的color_list
# 缺陷块表示为黑色
color_list = [QColor(0, 0, 0)]

N = 1000
for i in range(N - 1):
    colors = np.random.randint(0, 255, (3,))  # R G B
    color_list.append(QColor(colors[0], colors[1], colors[2]))


class myWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)
        self.setupUi(self)

        # 设置绘画内容
        self.draw = "empty"

        # 设置棋盘属性
        self.level = 0  # 棋盘级别
        self.dr = 0  # 缺陷横坐标
        self.dc = 0  # 缺陷纵坐标
        self.size = 0  # 大小 size = 2 ** level
        self.chessboard = None  # 填充结果
        self.length = 0  # 格子边长
        self.sides = 400  # 棋盘总长度

        # 绑定槽函数
        self.generate_Bn.clicked.connect(self.generate)
        self.clear_Bn.clicked.connect(self.clear)
        self.spinBox_level.valueChanged.connect(self.draw_line)

    # 绘制空的白板
    def empty(self):
        self.update()
        self.draw = "empty"

    # 根据chessboard绘制棋盘
    def board(self):
        self.update()
        self.draw = "board"

    # 根据棋盘大小绘制格子线
    def line(self):
        self.update()
        self.draw = "line"

    # 根据不同的self.draw属性，绘制不同图形
    def paintEvent(self, qp):
        qp = QPainter()
        if self.draw == 'empty':
            qp.begin(self)
            # 设置画笔画刷
            pen = QPen(Qt.black, 1, Qt.SolidLine)
            qp.setPen(pen)
            qp.setBrush(QColor(255, 255, 255))
            # 绘制白底黑框
            qp.drawRect(20, 20, self.sides, self.sides)
            qp.end()

        if self.draw == "line":
            qp.begin(self)

            # 设置画笔画刷
            pen = QPen(Qt.black, 1, Qt.SolidLine)
            qp.setPen(pen)
            qp.setBrush(QColor(255, 255, 255))
            # 画白框
            qp.drawRect(20, 20, self.sides, self.sides)
            # 根据格子边长画线
            for i in range(self.size):
                qp.drawLine(20, 20 + i * self.length, 20 + self.sides, 20 + i * self.length)  # 横线
                qp.drawLine(20 + i * self.length, 20, 20 + i * self.length, 20 + self.sides)  # 竖线

            qp.end()

        if self.draw == "board":
            qp = QPainter()
            qp.begin(self)
            # 设置画笔
            pen = QPen(Qt.black, 1, Qt.SolidLine)
            qp.setPen(pen)

            # 根据chessboard数值填充每个格子
            for i in range(self.size):
                for j in range(self.size):
                    qp.setBrush(color_list[int(self.chessboard[i][j] % len(color_list))])
                    qp.drawRect(20 + i * self.length, 20 + j * self.length, self.length, self.length)

            qp.end()

    # level数值改变时绘制新的棋盘
    def draw_line(self):
        self.level = self.spinBox_level.value()
        if self.level != 0:
            self.size = 2 ** self.level
            self.length = self.sides / self.size
            # 画线
            self.line()

    # 计算棋盘填充方案并可视化
    def generate(self):
        # 获取属性值
        level, dr, dc = self.spinBox_level.value(), self.spinBox_dr.value(), self.spinBox_dc.value()
        self.size = 2 ** level
        # 输入判断
        msg_box = QMessageBox(self)
        if level == 0:
            msg_box.information(self, "Warning", "棋盘级别不能为0！", QMessageBox.Yes)
        elif max(dr, dc) > self.size:
            msg_box.information(self, "Warning", "棋盘坐标不能超过棋盘大小！", QMessageBox.Yes)
        else:
            # 计算棋盘填充结果
            dc_board = DC(self.size, dr, dc)
            self.chessboard = dc_board.tile_board(0, 0, dr, dc, self.size)
            # 绘制棋盘
            self.board()

    # 清空画板及数值
    def clear(self):
        self.empty()
        self.spinBox_level.setValue(0)
        self.spinBox_dr.setValue(0)
        self.spinBox_dc.setValue(0)
