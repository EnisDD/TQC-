class SideError(ValueError) :
    pass
#定義例外類別

sides = {
    's1': int(input()),
    's2': int(input()),
    's3': int(input())
}
#用字典儲存3個邊長

def calculate(s1, s2, s3) :

    if s1 <= 0 :
        raise SideError(s1)
        #邊長<=0時報錯
    
    elif s2 <= 0 :
        raise SideError(s2)
        #邊長<=0時報錯
    
    elif s3 <= 0 :
        raise SideError(s3)
        #邊長<=0時報錯

    if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2 :

        print(s1 + s2 + s3)
        #如果任兩邊的和大於第三邊，輸出周長

    else :
        print('Invalid')

calculate(**sides)
#用**解包字典












