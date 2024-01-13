import math as mt
#匯入math
class DataError(ValueError) :
    pass
class SidenumberError(DataError) :
    pass
class SidelengthError(DataError) :
    pass
#定義例外類別

all_data = {'N_side' : eval(input()), 'Side_length' : eval(input())}
#用字典儲存邊的數量和邊長

def Area (N_side, Side_length):
   
   if N_side < 3 :
       raise SidenumberError(N_side)
       #當邊的數量小於3時報錯（沒有2邊型）
   
   elif Side_length == 0 :
       raise SidelengthError(Side_length)
       #當邊長為0時，面積為零，錯誤
    
   area = (N_side * mt.pow(Side_length, 2)) / (4 * mt.tan(mt.pi / N_side))
   #算面積

   print(f'Area = {area:.4f}')
   #輸出面積到小數點後4位

Area(**all_data)
#用**解包字典













