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