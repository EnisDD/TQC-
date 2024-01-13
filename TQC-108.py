import math

all_Data = {
    'x1': eval(input()),
    'y1': eval(input()),
    'x2': eval(input()),
    'y2': eval(input())
}
#用字典儲存兩個座標

def Distance(x1, x2, y1, y2) :
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #算距離
    print(f'( {x1} , {y1} )')
    #輸出第一個座標
    print(f'( {x2} , {y2} )')
    #輸出第二個座標
    print(f'Distance = {distance :.4f}')
    #輸出距離

Distance(**all_Data)
#用**解包字典










