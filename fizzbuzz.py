#1から100までの数をプリントするプログラムを書け。
# ただし3の倍数のときは数の代わりに｢Fizz｣と、5の倍数のときは｢Buzz｣とプリントし、
# 3と5両方の倍数の場合には｢FizzBuzz｣とプリントすること。


for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 15 == 0:
        print("FizzBuzz")
    else:
        print(i)        
    