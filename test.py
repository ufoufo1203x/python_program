for i in range(1, 101):
    # 3 and 5の倍数の時
    if i % 3 == 0 and i % 5 ==0:
        print('FizzBuzzz')
    #3の倍数の時
    elif i % 3 == 0:
        print('Fizz')
    #5の倍数の時
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)