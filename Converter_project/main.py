import sys
from PyQt5.QtWidgets import QApplication
from converter import ConverterWindow

app = QApplication(sys.argv)

converter = ConverterWindow()

sys.exit(app.exec_())