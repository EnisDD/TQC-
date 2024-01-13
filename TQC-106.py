
class DataError(ValueError):
    pass
class TimeError(DataError) :
    pass
class MinError(TimeError) :
    pass
class SecError(TimeError) :
    pass
class DistanceError(DataError) :
    pass
#定義例外類別
all_Data = {
    'min': float(input()),
    'sec': float(input()),
    'km': float(input())
}
#利用字典儲存min, sec, km

def speed(min, sec, km) :

    if min <= 0 :
        raise MinError(min)
        #時間不會小於等於0
    elif sec <= 0 :
        raise SecError(sec)
        #時間不會小於等於0
    elif km <= 0 :
        raise DistanceError(km)
        #距離不會為0
    
    UK_m = km / 1.6
    #換算英里
    time = min / 60 + sec / 3600
    #換算小時
    answer = UK_m / time
    #算速度
    print(f'Speed = {answer :.1f}')
    #輸出到小數點後一位

speed(**all_Data)
#用**解包字典













