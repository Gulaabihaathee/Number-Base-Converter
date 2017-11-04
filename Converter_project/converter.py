from PyQt5 import QtWidgets
from ui_converter import Ui_Converter
from math import floor

dic={'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
inv_dic = dict(zip(dic.values(), dic.keys()))
def dec_to_arb(Decimal_Number, Base):
	String = ""
	while(Decimal_Number != 0):
			String += str(dic[str(int(Decimal_Number%Base))])
			Decimal_Number = floor(Decimal_Number/Base)
	Converted_Number = String[::-1]
	return(Converted_Number)
		
def arb_to_dec(StringNumber, InBase):
	suma, I = 0, 1
	for i in StringNumber:
			suma += (int(inv_dic[i])*(InBase**(len(StringNumber)-I)))
			I += 1
	return(suma)


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
