from PyQt5 import QtWidgets
from ui_converter import Ui_Converter
from math_functions import *

class ConverterWindow(QtWidgets.QMainWindow, Ui_Converter):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
	
		#connect buttons
		self.ConvertButton.clicked.connect(self.button_pressed)
		
	def button_pressed(self):
	
		dic_list = list(dic.values())
		dic_list.sort()
		V = True
		for it in self.lineEdit.text():
			if((it in dic_list[:self.InBaseBox.value()]) == False):
				self.ResultBox.setText("Incorrect value!")
				V = False
		if(V == True):
			result = dec_to_arb(arb_to_dec(self.lineEdit.text(), self.InBaseBox.value()), self.OutBaseBox.value())
			button = self.sender()
			self.ResultBox.clear
			self.ResultBox.setText(result)
