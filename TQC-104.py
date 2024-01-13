import math
#匯入math
class RadiusError(ValueError) :
    pass
#定義例外類別

def Area(r) :

    if r <= 0 :
        raise RadiusError(r)
    #當半徑為0時報錯

    print(f'Radius = {r:.2f}')
    #輸出半徑
    print(f'Perimeter = {(r * 2 * math.pi):.2f}')
    #輸出周長
    print(f'Area = {(pow(r, 2) * math.pi):.2f}')
    #輸出面積

Area(r = float(input()))
#呼叫函式並輸入一個值