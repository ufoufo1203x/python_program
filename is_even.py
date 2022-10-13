def is_even():
    number = input('数字を指定してください:')
    if int(number) % 2 == 0:
        print('True')
    else:
        print('False')
    return
    
data = is_even()
print(data)