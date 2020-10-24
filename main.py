import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from myWindow import myWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = myWindow()
    myWin.show()
    sys.exit(app.exec_())
