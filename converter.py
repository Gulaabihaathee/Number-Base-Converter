#Arbitrary-base system converter
#Write in terminal: python3 converter.py Dec_num Base

from math import floor
import sys

dic={'0':'0','1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
Decimal_Number = int(sys.argv[1])
Base = int(sys.argv[2])
String = ""

while(Decimal_Number != 0):
	String += str(dic[str(int(Decimal_Number%Base))])
	Decimal_Number = floor(Decimal_Number/Base)

Converted_Number = String[::-1]
print(Converted_Number)
