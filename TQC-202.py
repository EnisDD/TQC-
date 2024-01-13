num = int(input())
#輸入一個整數

if num % 5 == 0  and num % 3 == 0:

    print(f'{num} is a multiple of 3 and 5.')
    #是3和5的公倍數
    
elif num % 3 == 0 :

    print(f'{num} is a multiple of 3.')
    #是3的倍數

elif num % 5 == 0 :

    print(f'{num} is a multiple of 5.')
    #是5的倍數

elif num % 3 != 0 and num % 5 != 0 :

    print(f'{num} is not a multiple of 3 or 5.')
    #不是3和5的倍數